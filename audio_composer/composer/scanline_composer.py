from collections import defaultdict

from audio_composer.models.audioclip import AudioClip
from audio_composer.models.audiotrack import AudioTrack


def scanline_composer(
    segments: list[AudioClip],
) -> dict[int, list[AudioClip]]:
    """
    将片段分配到轨道，确保开始时间相同的片段尽量在连续轨道上。
    改进版本：优先复用已释放的轨道，减少轨道数量。

    参数:
        segments: 需要分配的片段列表。
    返回:
        字典，键为轨道编号（从1开始），值为该轨道的片段列表。
    """
    if not segments:
        return {}

    # 按开始时间分组
    start_time_groups: defaultdict[float, list[AudioClip]] = defaultdict(list)
    for clip in segments:
        start_time_groups[clip.start_offset].append(clip)

    # 按开始时间排序分组
    sorted_groups = sorted(start_time_groups.items(), key=lambda x: x[0])

    # 初始化轨道
    tracks: dict[int, list[AudioClip]] = {}  # 轨道编号到片段列表的映射
    track_end_times: dict[int, float] = {}  # 轨道编号到最后一个片段结束时间的映射
    next_track_id: int = 1  # 下一个可用轨道ID

    # 使用优先队列管理可用轨道（按轨道ID排序）
    available_tracks = []  # 已释放的轨道ID列表

    # 为每个分组分配轨道
    for start_time, group in sorted_groups:
        group_size = len(group)

        # 1. 清理已释放的轨道（结束时间 <= 当前开始时间）
        released_tracks = []
        for track_id, end_time in track_end_times.items():
            if end_time <= start_time:
                released_tracks.append(track_id)

        # 将释放的轨道添加到可用轨道列表
        for track_id in released_tracks:
            if track_id not in available_tracks:
                available_tracks.append(track_id)
                available_tracks.sort()  # 保持有序

        # 2. 寻找需要的轨道数量
        needed_tracks = []

        # 首先尝试使用已释放的轨道
        while available_tracks and len(needed_tracks) < group_size:
            track_id = available_tracks.pop(0)  # 取最小的轨道ID
            needed_tracks.append(track_id)

        # 如果还需要更多轨道，创建新轨道
        while len(needed_tracks) < group_size:
            needed_tracks.append(next_track_id)
            next_track_id += 1

        # 3. 将组内片段分配到轨道
        for clip, track_id in zip(group, needed_tracks):
            if track_id not in tracks:
                tracks[track_id] = []
            tracks[track_id].append(clip)
            track_end_times[track_id] = clip.end_offset

    return tracks


def scanline_composer_optimized(
    segments: list[AudioClip],
) -> dict[int, list[AudioClip]]:
    """
    优化的扫描线算法，进一步减少轨道数量。
    使用更智能的轨道分配策略，包括连续性优化和轨道压缩。

    参数:
        segments: 需要分配的片段列表。
    返回:
        字典，键为轨道编号（从1开始），值为该轨道的片段列表。
    """
    if not segments:
        return {}

    # 按开始时间分组
    start_time_groups: defaultdict[float, list[AudioClip]] = defaultdict(list)
    for clip in segments:
        start_time_groups[clip.start_offset].append(clip)

    # 按开始时间排序分组
    sorted_groups = sorted(start_time_groups.items(), key=lambda x: x[0])

    # 初始化轨道
    tracks: dict[int, list[AudioClip]] = {}  # 轨道编号到片段列表的映射
    track_end_times: dict[int, float] = {}  # 轨道编号到最后一个片段结束时间的映射
    next_track_id: int = 1  # 下一个可用轨道ID

    # 使用优先队列管理可用轨道（按轨道ID排序）
    available_tracks = []  # 已释放的轨道ID列表

    # 为每个分组分配轨道
    for start_time, group in sorted_groups:
        group_size = len(group)

        # 1. 清理已释放的轨道（结束时间 <= 当前开始时间）
        released_tracks = []
        for track_id, end_time in track_end_times.items():
            if end_time <= start_time:
                released_tracks.append(track_id)

        # 将释放的轨道添加到可用轨道列表
        for track_id in released_tracks:
            if track_id not in available_tracks:
                available_tracks.append(track_id)
                available_tracks.sort()  # 保持有序

        # 2. 智能轨道分配策略
        needed_tracks = []

        # 策略1: 优先使用已释放的轨道
        while available_tracks and len(needed_tracks) < group_size:
            track_id = available_tracks.pop(0)  # 取最小的轨道ID
            needed_tracks.append(track_id)

        # 策略2: 如果还需要轨道，尝试寻找连续的空闲轨道
        if len(needed_tracks) < group_size:
            remaining_needed = group_size - len(needed_tracks)

            # 寻找连续的空闲轨道
            continuous_tracks = []
            current_continuous = []

            for track_id in range(1, next_track_id):
                if (
                    track_id not in track_end_times
                    or track_end_times[track_id] <= start_time
                ):
                    current_continuous.append(track_id)
                    if len(current_continuous) == remaining_needed:
                        continuous_tracks = current_continuous
                        break
                else:
                    current_continuous = []

            # 如果找到足够的连续轨道，使用它们
            if len(continuous_tracks) == remaining_needed:
                needed_tracks.extend(continuous_tracks)
            else:
                # 否则创建新轨道
                while len(needed_tracks) < group_size:
                    needed_tracks.append(next_track_id)
                    next_track_id += 1

        # 3. 将组内片段分配到轨道
        for clip, track_id in zip(group, needed_tracks):
            if track_id not in tracks:
                tracks[track_id] = []
            tracks[track_id].append(clip)
            track_end_times[track_id] = clip.end_offset

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

    # 使用优化的 scanline_composer 分配轨道
    track_assignment = scanline_composer_optimized(clips)

    # 将分配结果转换回 AudioTrack 对象
    tracks: list[AudioTrack] = []
    for track_num, track_clips in sorted(track_assignment.items()):
        # 创建 AudioTrack，轨道索引从 1 开始，与原函数的命名约定一致
        track = AudioTrack(character=character, index=track_num, clips=track_clips)
        tracks.append(track)

    return tracks
