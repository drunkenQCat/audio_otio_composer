import click
from datetime import datetime
from audio_composer.composer.audio_to_timeline import (
    audio_to_tracks,
    get_audio_clips,
)
from audio_composer.models.audiotrack import AudioTrack
from audio_composer.models.audioclip import MODE_MIX, MODE_RESOLVE, MODE_PREMIERE
import opentimelineio as otio
from opentimelineio.core import Track
from opentimelineio.schema import Timeline
from opentimelineio.opentime import TimeRange, to_frames, RationalTime

from premiere_pro.pr_metadata import (
    make_timeline_metadata,
    make_stack_metadata,
    make_audio_track_metadata,
)
from premiere_pro.pr_effects import add_pr_track_effects
from utils.logger import logger

VALID_MODES = (MODE_MIX, MODE_RESOLVE, MODE_PREMIERE)


def create_timeline(
    global_start_hour: int, fps: float, metadata_mode: str = MODE_MIX
) -> Timeline:
    """
    创建一个新的 OTIO 时间轴并设置元数据和全局起始时间。

    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    :param metadata_mode: metadata 模式 ('mix', 'resolve', 'premiere')。
    :return: 一个 OTIO 时间轴实例。
    """
    timeline = Timeline()
    timeline.name = "Audio Timeline"

    # 设置全局起始时间
    seconds = global_start_hour * 60**2
    hour_one_frames = to_frames(RationalTime(value=seconds), rate=fps)
    timeline.global_start_time = RationalTime(hour_one_frames, fps)

    # 根据模式添加 metadata
    if metadata_mode in (MODE_MIX, MODE_RESOLVE):
        timeline.metadata["Resolve_OTIO"] = {"Resolve OTIO Meta Version": "1.0"}
    if metadata_mode in (MODE_MIX, MODE_PREMIERE):
        timeline.metadata.update(make_timeline_metadata())

    return timeline


def create_audio_track(
    track: AudioTrack, fps: float, metadata_mode: str = MODE_MIX
) -> Track:
    """
    创建一个 OTIO 音频轨道。

    :param track: AudioTrack 对象。
    :param fps: 帧率。
    :param metadata_mode: metadata 模式。
    :return: OTIO Track 实例。
    """
    tr = Track(track.track_name, kind="Audio")

    # 从第一个非 Gap 的 clip 获取通道数
    channel_count = 1
    for clip in track.clips:
        if clip.character != "gap":
            channel_count = clip.channel_count
            break

    # Resolve metadata
    if metadata_mode in (MODE_MIX, MODE_RESOLVE):
        audio_type = "Stereo" if channel_count == 2 else "Mono"
        tr.metadata["Resolve_OTIO"] = {
            "Audio Type": audio_type,
            "Locked": False,
            "SoloOn": False,
        }

    # Premiere Pro metadata
    if metadata_mode in (MODE_MIX, MODE_PREMIERE):
        tr.metadata.update(make_audio_track_metadata(channel_count))
        # Premiere Pro track effects
        add_pr_track_effects(tr, fps)

    for clip in track.clips:
        tr.append(clip.clip)
    return tr


def set_track_source_range(track: Track, start_time: RationalTime):
    """
    将轨道的来源范围设置为与全局起始时间匹配。

    :param track: 要更新的 OTIO 轨道。
    :param start_time: 要设置的起始时间。
    """
    track.source_range = TimeRange(start_time, track.duration())


def make_otio(
    audio_tracks: list[AudioTrack],
    global_start_hour: int = 0,
    fps: float = 24.0,
    output: str = "",
    metadata_mode: str = MODE_MIX,
):
    """
    生成 OTIO 时间轴。

    :param audio_tracks: 音频轨道列表。
    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    :param output: 输出文件名。
    :param metadata_mode: metadata 模式。
    """
    logger.info(f"start to export otio file (mode: {metadata_mode}) ...")
    timeline = create_timeline(global_start_hour, fps, metadata_mode)

    # Stack metadata
    if metadata_mode in (MODE_MIX, MODE_PREMIERE):
        timeline.tracks.metadata.update(make_stack_metadata(fps=fps))
        timeline.tracks.name = output

    # 占位视频轨道
    timeline.tracks.append(Track(name="Video 1"))

    # 音频轨道（不在 OTIO Track 上设置 source_range，PR 需要 null）
    tracks = [create_audio_track(tr, fps, metadata_mode) for tr in audio_tracks]
    for track in tracks:
        timeline.tracks.append(track)

    # 写入 OTIO 文件
    output_path = f"{output}.otio"
    otio.adapters.write_to_file(timeline, output_path)

    # Premiere 模式需要后处理：添加 enabled=true（OTIO 库默认不序列化 enabled=True）
    if metadata_mode in (MODE_MIX, MODE_PREMIERE):
        _patch_effects_enabled(output_path)

    logger.info("Finished!!")


def _patch_effects_enabled(filepath: str):
    """后处理：给所有 Effect 添加 enabled=true 字段。

    OTIO 库在 enabled=True（默认值）时不序列化该字段，
    但 PR 导入器期望看到显式的 enabled 字段。
    """
    import json

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    def _walk_set_enabled(obj):
        if isinstance(obj, dict):
            if obj.get("OTIO_SCHEMA", "").startswith("Effect."):
                if "enabled" not in obj:
                    obj["enabled"] = True
            for v in obj.values():
                _walk_set_enabled(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk_set_enabled(item)

    _walk_set_enabled(data)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


@click.command()
@click.option(
    "--path",
    "-p",
    default="test_data",
    help="输入数据路径，通常是包含音频文件的文件夹路径。",
)
@click.option("--output", "-o", help="输出文件名，用于生成 OTIO 时间轴文件。")
@click.option("--fps", "-f", type=float, default=24.0, help="帧率")
@click.option(
    "--metadata-mode",
    "-m",
    type=click.Choice(["mix", "resolve", "premiere"]),
    default="mix",
    help="metadata 模式: mix=同时包含 Resolve+PR, resolve=仅 Resolve, premiere=仅 PR",
)
def main(path: str, output: str | None = None, fps: float = 24.0, metadata_mode: str = "mix"):
    """
    主函数，用于生成具有用户定义参数的 OTIO 时间轴。

    :param path: 输入数据路径。
    :param output: 输出文件名。
    :param fps: 帧率。
    :param metadata_mode: metadata 模式。
    """
    if output is None:
        output = "test_data"
    else:
        now = datetime.now().strftime("%y%m%d_%H%M")
        output = f"{output}_{now}"

    global_start_hour = 0

    audio_list = get_audio_clips(path, fps=fps, metadata_mode=metadata_mode)
    tracks = audio_to_tracks(audio_list, fps=fps)
    make_otio(tracks, global_start_hour, fps, output, metadata_mode)


if __name__ == "__main__":
    main()
