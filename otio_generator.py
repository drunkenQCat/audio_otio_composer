#! /usr/bin/env python

# Populate OpenTimelineIO timeline with randomly generated clips.
# Export to common NLE formats.
# igor at hdead.com

import opentimelineio as otio
from opentimelineio.core import Track
from opentimelineio.schema import Gap, Clip, ExternalReference, Timeline
from opentimelineio.opentime import TimeRange, to_frames, RationalTime
from random import randint, choice
import os
import string
import datetime


def _rand_string(r=10):
    letters = string.ascii_lowercase
    randString = "".join(choice(letters) for i in range(r))

    return randString


def create_timeline(global_start_hour: int, fps: int) -> Timeline:
    """
    创建一个新的 OTIO 时间轴并设置元数据和全局起始时间。

    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    :return: 一个 OTIO 时间轴实例。
    """
    # 创建时间轴实例并设置名称
    timeline = Timeline()
    timeline.name = "Generated with randomotio.py"

    # 设置全局起始时间
    seconds = global_start_hour * 60**2
    hour_one_frames = to_frames(RationalTime(value=seconds), rate=fps)
    timeline.global_start_time = RationalTime(hour_one_frames, fps)

    # 添加元数据
    timeline.metadata["Random OTIO"] = {"version": "0.1.0"}
    return timeline


def create_tracks(trk_count: int) -> list[Track]:
    """
    创建指定数量的空 OTIO 轨道。

    :param trk_count: 要创建的轨道数量。
    :return: 一个包含 OTIO 轨道实例的列表。
    """
    # 创建指定数量的轨道
    return [Track() for _ in range(trk_count)]


def populate_track_with_clips(track: Track, clp_count: int, fps: int, max_tc: int):
    """
    为指定的轨道添加剪辑和间隙。

    :param track: 要填充的 OTIO 轨道。
    :param clp_count: 要添加到轨道中的剪辑数量。
    :param fps: 剪辑的帧率。
    :param max_tc: 剪辑来源范围的最大时间码。
    """
    for _ in range(clp_count):
        clip = create_random_clip(fps, max_tc)
        track.append(clip)

        # TODO: 还要在Resource里提前算好Gap，不，直接做成dict[str, dict[Clip/ExternalReference, Gap]]
        # 创建随机间隙 (Gap)
        if randint(0, 1) == 1:
            gap = Gap()
            if clip.source_range is None:
                continue
            gap_duration = clip.source_range.duration
            gap.source_range = TimeRange(duration=gap_duration)
            gap.name = "Black"
            track.append(gap)


def create_random_clip(fps: int, max_tc: int) -> Clip:
    """
    创建一个带有随机元数据和媒体引用的 OTIO 剪辑。

    :param fps: 剪辑的帧率。
    :param max_tc: 剪辑来源范围的最大时间码。
    :return: 一个 OTIO 剪辑实例。
    """
    clip = Clip()

    # 随机生成剪辑名称
    clip_name = _rand_string()
    clip.name = clip_name

    # 设置剪辑的来源范围
    min_dur = 1
    max_dur = int(10 * fps)
    tc_in = randint(0, max_tc)
    # TODO: duration转换
    duration = randint(min_dur, max_dur)

    clip.source_range = TimeRange(
        start_time=RationalTime(tc_in, fps),
        duration=RationalTime(duration, fps),
    )

    # 添加虚拟媒体引用
    rand_path1 = _rand_string(8)
    rand_path2 = _rand_string(4)
    # TODO: 音频文件路径
    url = os.path.join(
        "/Volumes", "FakeProject", rand_path1, rand_path2, clip_name + ".mov"
    )

    # TODO: 从fcpxml的Resource那儿偷代码，先做一个dict[str, ExternalReference]
    clip.media_reference = ExternalReference(
        target_url=url,
        available_range=TimeRange(
            start_time=RationalTime(0, fps),
            duration=RationalTime(86400, fps),
        ),
    )

    # TODO: 写上我的大名
    # 添加剪辑元数据
    timestamp = datetime.datetime.now()
    clip.metadata["Random OTIO"] = {
        "Creation Time": str(timestamp),
        "Generated By": "randomotio.py",
    }

    return clip


def set_track_source_range(track: Track, start_time: RationalTime):
    """
    将轨道的来源范围设置为与全局起始时间匹配。

    :param track: 要更新的 OTIO 轨道。
    :param start_time: 要设置的起始时间。
    """
    track.source_range = TimeRange(start_time, track.duration())


def make_otio(trk_count: int, clp_count: int, global_start_hour: int, fps: int):
    """
    生成一个包含随机轨道和剪辑的 OTIO 时间轴。

    :param trk_count: 要创建的轨道数量。
    :param clp_count: 每个轨道的剪辑数量。
    :param global_start_hour: 时间轴的全局起始时间（小时）。
    :param fps: 时间轴的帧率。
    """
    timeline = create_timeline(global_start_hour, fps)
    tracks = create_tracks(trk_count)

    # 每个轨道中填充随机剪辑和间隙
    hour_one_frames = to_frames(RationalTime(global_start_hour * 60**2), rate=fps)
    for track in tracks:
        # TODO: 改成角色名-序号
        track.name = f"V{tracks.index(track) + 1}"
        populate_track_with_clips(track, clp_count, fps, hour_one_frames)
        set_track_source_range(track, RationalTime(-hour_one_frames, fps))
        timeline.tracks.append(track)

    # 输出 OTIO 文件
    otio.adapters.write_to_file(timeline, "random.otio")

    # 可以根据需要输出其他格式
    # otio.adapters.write_to_file(timeline, 'random.xml')
    # if trk_count == 1:
    #     otio.adapters.write_to_file(timeline, 'random.edl')


def main():
    """
    主函数，用于生成具有用户定义参数的随机 OTIO 时间轴。
    """
    # 设置参数
    trk_count = 3  # 轨道数量
    clp_count = 5  # 每个轨道的剪辑数量
    global_start_hour = 1  # 时间轴全局起始时间（小时）
    fps = 24  # 帧率

    # 调用主函数生成时间轴
    make_otio(trk_count, clp_count, global_start_hour, fps)


if __name__ == "__main__":
    main()