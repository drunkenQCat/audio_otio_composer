import click
from datetime import datetime
from audio_composer.composer.audio_to_timeline import audio_to_tracks, get_audio_clips
from audio_composer.models.audiotrack import AudioTrack
import opentimelineio as otio
from opentimelineio._otio import Gap
from opentimelineio.core import Track
from opentimelineio.schema import Timeline
from opentimelineio.opentime import TimeRange, to_frames, RationalTime

from utils.logger import logger


def create_timeline(global_start_hour: int, fps: float) -> Timeline:
    """
    创建一个新的 OTIO 时间轴并设置元数据和全局起始时间。

    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    :return: 一个 OTIO 时间轴实例。
    """
    # 创建时间轴实例并设置名称
    timeline = Timeline()

    # 设置全局起始时间
    seconds = global_start_hour * 60**2
    hour_one_frames = to_frames(RationalTime(value=seconds), rate=fps)
    timeline.global_start_time = RationalTime(hour_one_frames, fps)

    # 添加元数据
    timeline.metadata["Resolve_OTIO"] = {"Resolve OTIO Meta Version": "1.0"}
    return timeline


def create_audio_track(track: AudioTrack) -> Track:
    """
    创建指定数量的空 OTIO 轨道。

    :param trk_count: 要创建的轨道数量。
    :return: 一个包含 OTIO 轨道实例的列表。
    """
    # 创建指定数量的轨道
    tr = Track(track.track_name, kind="Audio")
    tr.metadata["Resolve_OTIO"] = {
        "Audio Type": "Mono",
        "Locked": False,
        "SoloOn": False,
    }
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


def generate_first_empty_track(duration: float = 576) -> Track:
    tr = Track(name="Video 1")
    tr.metadata["Resolve_OTIO"] = {"Locked": False}

    gap = Gap()
    time_range = TimeRange(duration=RationalTime(rate=24, value=duration))
    gap.source_range = time_range

    tr.append(gap)

    return tr


def make_otio(
    audio_tracks: list[AudioTrack],
    global_start_hour: int = 0,
    fps: float = 24.0,
    output: str = "",
):
    """
    生成一个包含随机轨道和剪辑的 OTIO 时间轴。

    :param trk_count: 要创建的轨道数量。
    :param clp_count: 每个轨道的剪辑数量。
    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    """
    logger.info("start to export otio file ...")
    timeline = create_timeline(global_start_hour, fps)
    # 添加一个占位用的视频轨道
    timeline.tracks.append(Track(name="Video 1"))
    tracks = [create_audio_track(tr) for tr in audio_tracks]

    hour_one_frames = to_frames(RationalTime(global_start_hour * 60**2), rate=fps)
    for track in tracks:
        set_track_source_range(track, RationalTime(-hour_one_frames, fps))
        timeline.tracks.append(track)

    # 输出 OTIO 文件
    otio.adapters.write_to_file(timeline, f"{output}.otio")
    logger.info("Finished!!")


@click.command()
@click.option(
    "--path",
    "-p",
    default="test_data",
    help="输入数据路径，通常是包含音频文件的文件夹路径。",
)
@click.option("--output", "-o", help="输出文件名，用于生成 OTIO 时间轴文件。")
@click.option("--fps", "-f", type=float, default=24.0, help="帧率")
def main(path: str, output: str | None = None, fps: float = 24.0):
    """
    主函数，用于生成具有用户定义参数的随机 OTIO 时间轴。

    :param path: 输入数据路径，通常是包含音频文件的文件夹路径。

    :param output: 输出文件名，用于生成 OTIO 时间轴文件。没有提供时，默认使用 "test_data"。
    """
    # 设置参数
    if output is None:
        # 默认工程名
        output = "test_data"
    else:
        now = datetime.now().strftime("%y%m%d_%H%M")
        output = f"{output}_{now}"

    global_start_hour = 0  # 时间轴全局起始时间（小时）

    # 调用主函数生成时间轴
    audio_list = get_audio_clips(path, fps=fps)
    tracks = audio_to_tracks(audio_list)
    make_otio(tracks, global_start_hour, fps, output)


if __name__ == "__main__":
    main()
