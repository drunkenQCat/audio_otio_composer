from audio_to_timeline import audio_to_tracks, get_audio_clips
from models.audiotrack import AudioTrack
import opentimelineio as otio
from opentimelineio.core import Track
from opentimelineio.schema import Timeline
from opentimelineio.opentime import TimeRange, to_frames, RationalTime


def create_timeline(global_start_hour: int, fps: int) -> Timeline:
    """
    创建一个新的 OTIO 时间轴并设置元数据和全局起始时间。

    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    :return: 一个 OTIO 时间轴实例。
    """
    # 创建时间轴实例并设置名称
    timeline = Timeline()
    timeline.name = "Generated with Audio Otio Composer"

    # 设置全局起始时间
    seconds = global_start_hour * 60**2
    hour_one_frames = to_frames(RationalTime(value=seconds), rate=fps)
    timeline.global_start_time = RationalTime(hour_one_frames, fps)

    # 添加元数据
    timeline.metadata["Audio Otio Composer"] = {"version": "0.1.0"}
    return timeline


def create_track(track: AudioTrack) -> Track:
    """
    创建指定数量的空 OTIO 轨道。

    :param trk_count: 要创建的轨道数量。
    :return: 一个包含 OTIO 轨道实例的列表。
    """
    # 创建指定数量的轨道
    tr = Track(track.track_name)
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
    audio_tracks: list[AudioTrack], global_start_hour: int = 0, fps: int = 24
):
    """
    生成一个包含随机轨道和剪辑的 OTIO 时间轴。

    :param trk_count: 要创建的轨道数量。
    :param clp_count: 每个轨道的剪辑数量。
    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    """
    print("start to export otio file ...")
    timeline = create_timeline(global_start_hour, fps)
    tracks = [create_track(tr) for tr in audio_tracks]

    hour_one_frames = to_frames(RationalTime(global_start_hour * 60**2), rate=fps)
    for track in tracks:
        set_track_source_range(track, RationalTime(-hour_one_frames, fps))
        timeline.tracks.append(track)

    # 输出 OTIO 文件
    otio.adapters.write_to_file(timeline, "project.otio")
    print("Finished!!")


def main():
    """
    主函数，用于生成具有用户定义参数的随机 OTIO 时间轴。
    """
    # 设置参数
    global_start_hour = 0  # 时间轴全局起始时间（小时）
    fps = 24  # 帧率

    # 调用主函数生成时间轴
    audio_list = get_audio_clips("test_data")
    tracks = audio_to_tracks(audio_list)
    make_otio(tracks, global_start_hour, fps)


if __name__ == "__main__":
    main()
