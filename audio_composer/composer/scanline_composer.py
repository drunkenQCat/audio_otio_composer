from collections import defaultdict

from audio_composer.models.audioclip import AudioClip
from audio_composer.models.audiotrack import AudioTrack


def scanline_composer(
    segments: list[AudioClip],
) -> dict[int, list[AudioClip]]:
    """
    将片段分配到轨道，确保开始时间相同的片段尽量在连续轨道上。
    如果找不到连续的可用轨道，会动态添加新轨道。

    参数:
        segments: 需要分配的片段列表。
    返回:
        字典，键为轨道编号（从1开始），值为该轨道的片段列表。
    """
    # 按开始时间分组
    start_time_groups: defaultdict[float, list[AudioClip]] = defaultdict(list)
    for clip in segments:
        start_time_groups[clip.start_offset].append(clip)

    # 按开始时间排序分组
    sorted_groups = sorted(start_time_groups.items(), key=lambda x: x[0])

    # 初始化轨道
    tracks: dict[int, list[AudioClip]] = {}  # 轨道编号到片段列表的映射
    track_end_times: dict[int, float] = {}  # 轨道编号到最后一个片段结束时间的映射
    current_track_count: int = 0  # 当前轨道数

    # 为每个分组分配连续轨道
    for start_time, group in sorted_groups:
        """
        Closures Start
        """

        def is_track_spare(current_track_num):
            return (
                current_track_num not in track_end_times
                or track_end_times[current_track_num] <= start_time
            )

        def find_continuous_tracks():
            available_tracks: list[int] = []
            for track_num in range(1, current_track_count + 1):
                if not is_track_spare(track_num):
                    return []  # 如果当前轨道不可用，重置连续性
                available_tracks.append(track_num)
                if len(available_tracks) == group_size:
                    break
            return available_tracks

        """
        Closures End
        """
        group_size = len(group)
        # 寻找连续的可用轨道
        available_tracks: list[int] = find_continuous_tracks()
        # 如果连续轨道不足，添加新轨道
        while len(available_tracks) < group_size:
            current_track_count += 1
            available_tracks.append(current_track_count)
            tracks[current_track_count] = []
            track_end_times[current_track_count] = float("-inf")

        # 将组内片段分配到轨道
        for clip, track_num in zip(group, available_tracks):
            if track_num not in tracks:
                tracks[track_num] = []
            tracks[track_num].append(clip)
            track_end_times[track_num] = clip.end_offset

    return tracks


def generate_no_overlap_tracks(
    character: str, clips: list[AudioClip]
) -> list[AudioTrack]:
    """
    生成不重叠的音轨，确保开始时间相同的剪辑尽量在连续轨道上。

    参数:
        character: 角色名称。
        clips: 音频剪辑列表。
    返回:
        list[AudioTrack]: 生成的不重叠音轨列表。
    """
    # 按开始时间排序，与原函数保持一致
    clips.sort(key=lambda clip: clip.start_offset)

    # 使用 assign_tracks_with_continuous_grouping 分配轨道
    track_assignment = scanline_composer(clips)

    # 将分配结果转换回 AudioTrack 对象
    tracks: list[AudioTrack] = []
    for track_num, track_clips in sorted(track_assignment.items()):
        # 找到对应于 assigned_segments 的 AudioClip
        # 创建 AudioTrack，轨道索引从 1 开始，与原函数的命名约定一致
        track = AudioTrack(character=character, index=track_num, clips=track_clips)
        tracks.append(track)

    return tracks
