from dataclasses import dataclass
from pathlib import Path
import heapq

from models.audioclip import AudioClip, AudioGap
from models.audiotrack import AudioTrack, CharacterGroup


def get_audio_clips(folder: str) -> list[AudioClip]:
    """
    从指定文件夹中获取所有音频剪辑。

    参数:
        folder (str): 包含音频文件的文件夹路径。

    返回:
        list[AudioClip]: AudioClip 对象的列表。
    """
    audio_clips = []
    folder_path = Path(folder)
    for audio_file in folder_path.glob("**/*.wav"):
        clip = AudioClip(audio_file=str(audio_file))
        audio_clips.append(clip)
    return audio_clips


def group_clips_by_character(
    clips: list[AudioClip],
) -> list[tuple[str, list[AudioClip]]]:
    """
    根据角色将音频剪辑进行分组。

    参数:
        clips (list[AudioClip]): 音频剪辑的列表。

    返回:
        list[tuple[str, list[AudioClip]]]: 按角色分组的音频剪辑列表。
    """
    groups = {}
    for clip in clips:
        character = clip.character
        if character not in groups:
            groups[character] = []
        groups[character].append(clip)
    return list(groups.items())


def organize_tracks_by_character(
    clip_groups: list[tuple[str, list[AudioClip]]]
) -> list[CharacterGroup]:
    """
    根据角色组织音频剪辑分组为角色组，并将其规整到相应轨道上。

    参数:
        clip_groups (list[tuple[str, list[AudioClip]]]): 按角色分组的音频剪辑列表。

    返回:
        list[CharacterGroup]: 角色组的列表。
    """
    character_groups: list[CharacterGroup] = []
    for character, clips in clip_groups:
        tracks = generate_no_overlap_tracks(character, clips)
        group = CharacterGroup(character=character, tracks=tracks)
        character_groups.append(group)
    return character_groups


@dataclass(order=True)
class EndPoint:
    """
    用于指代生成轨道过程中的最远点
    """

    end_time: float
    track_idx: int


def generate_no_overlap_tracks(
    character: str, clips: list[AudioClip]
) -> list[AudioTrack]:
    """
    生成不重叠的音轨。

    参数:
        clips_with_character (tuple[str, list[AudioClip]]): 角色名称及其对应的音频剪辑。

    返回:
        AudioTrack: 生成的不重叠音轨。
    """

    # 按时间码排序
    clips.sort(key=lambda clip: clip.start_offset)

    #
    heap_of_endpoints: list[EndPoint] = []
    tracks: list[AudioTrack] = []

    def get_new_track_name():
        return len(tracks) + 1

    def get_new_track_id():
        return len(tracks) - 1

    """
    算法用例（轨道分配示例）：

    输入的音频片段及其起始和结束时间：
    1: [0, 5]
    2: [3, 6]
    3: [6, 8]
    4: [8, 11]
    5: [6, 10]

    分配过程：
    1. 初始化：轨道列表为空，优先队列 lq=[]。

    2. 添加片段 [0, 5]：
    - 当前无轨道，创建新轨道 1 并添加该片段。
    - 更新优先队列 lq = [(5, 1)] （结束时间为 5，属于轨道 1）。
    
    轨道分布：
    轨道 1: [0, 5]
    轨道 2: 空

    3. 添加片段 [3, 6]：
    - 片段 [3, 6] 的起始时间 3 小于轨道 1 的结束时间 5，无法放入轨道 1。
    - 创建新轨道 2 并添加该片段。
    - 更新优先队列 lq = [(5, 1), (6, 2)]。
    
    轨道分布：
    轨道 1: [0, 5]
    轨道 2: [3, 6]

    4. 添加片段 [6, 8]：
    - 片段 [6, 8] 的起始时间 6 大于轨道 1 的结束时间 5，可放入轨道 1。
    - 更新轨道 1，并更新优先队列 lq = [(6, 2), (8, 1)]。

    轨道分布：
    轨道 1: [0, 5], [6, 8]
    轨道 2: [3, 6]

    5. 添加片段 [8, 11]：
    - 片段 [8, 11] 的起始时间 8 大于轨道 1 的结束时间 8，可放入轨道 1。
    - 更新轨道 1，并更新优先队列 lq = [(10, 2), (11, 1)]。

    轨道分布：
    轨道 1: [0, 5], [6, 8], [8, 11]
    轨道 2: [3, 6]

    6. 添加片段 [6, 10]：
    - 片段 [6, 10] 的起始时间 6 小于轨道 2 的结束时间 6，但可与轨道 2 相接。
    - 更新轨道 2，并更新优先队列 lq = [(11, 1), (10, 2)]。

    轨道分布：
    轨道 1: [0, 5], [6, 8], [8, 11]
    轨道 2: [3, 6], [6, 10]

    最终结果：
    轨道 1: 11111###33444
    轨道 2: ###2225555#
    """
    no_tracks = True
    for clip in clips:
        if tracks and heap_of_endpoints[0].end_time <= clip.start_offset:
            print(f"{clip.start_offset}, not overlap")
            # 没有重叠
            last_endpoint = heapq.heappop(heap_of_endpoints)
            print(f"now pop {last_endpoint}")
            last_track_id = last_endpoint.track_idx
            tracks[last_track_id].clips.append(clip)
            print(
                f"add {clip.start_offset}, {clip.end_offset} to track{last_track_id + 1}"
            )
            heapq.heappush(heap_of_endpoints, EndPoint(clip.end_offset, last_track_id))
            print(f"the heap now :{heap_of_endpoints}")
            print(f"!!!!the clip count of first track is {len(tracks[0].clips)}!!!!")
        else:
            # 重叠了
            print(f"{clip.start_offset}, {clip.end_offset} overlap")
            new_track = AudioTrack(character=character, index=get_new_track_name())
            new_track.clips.append(clip)
            if no_tracks:
                print("--------------------------------------------------")
                print("the new track has been created, here's the first clip")
                __import__("pprint").pprint(new_track.clips)
                print(f"the clip count of track is {len(new_track.clips)}")
                no_tracks = False
            tracks.append(new_track)
            current_heap_info = EndPoint(clip.end_offset, get_new_track_id())
            print(f"{current_heap_info} added to the heap")
            heapq.heappush(heap_of_endpoints, current_heap_info)
            print("now the heap:")
            __import__("pprint").pprint(heap_of_endpoints)
            print(f"!!!!the clip count of first track is {len(tracks[0].clips)}!!!!")

    print("--------------------------------------------------")
    print(f"compose end, the clip count of first track is {len(tracks[0].clips)}")
    print(f"the track count is {len(tracks)}")
    print("--------------------------------------------------")
    return tracks


def generate_gap(duration: float) -> AudioGap:
    """
    生成一个音频间隙。

    参数:
        duration (float): 间隙的持续时间（秒）。

    返回:
        AudioClip: 生成的间隙音频剪辑。
    """
    gap = AudioGap(duration=duration)

    return gap


def generate_gaps_between_clips(clips: list[AudioClip]) -> list[AudioClip]:
    """
    根据AudioClip.offset_seconds，计算轨道上所有音频片段之间应当填充的间隙长度，
    并在在音频剪辑之间插入间隙。

    参数:
        clips (list[AudioClip]): 原始音频剪辑列表。

    返回:
        list[AudioClip]: 插入间隙后的音频剪辑列表。
    """
    clips_with_gaps: list[AudioClip] = []
    previous_offset = 0
    for clip in clips:
        gap_duration = clip.start_offset - previous_offset
        gap = generate_gap(gap_duration)

        clips_with_gaps += [gap, clip]
        previous_offset = clip.end_offset
    return clips_with_gaps


def flatten_chara_grps(chara_grps: list[CharacterGroup]) -> list[AudioTrack]:
    """
    将角色组转换为音轨列表。

    参数:
        chara_grps (list[CharacterGroup]): 角色组的列表。

    返回:
        list[AudioTrack]: 转换后的音轨列表。
    """
    audio_tracks: list[AudioTrack] = []
    for group in chara_grps:
        audio_tracks += group.tracks
    return audio_tracks


def audio_to_tracks(clips: list[AudioClip]) -> list[AudioTrack]:
    """
    将音频剪辑列表转换为音轨列表。

    参数:
        clips (list[AudioClip]): 输入的音频剪辑列表。

    返回:
        list[AudioTrack]: 转换后的音轨列表。
    """
    # 按角色分组音频剪辑
    clip_groups = group_clips_by_character(clips)

    # 组织角色组
    character_groups = organize_tracks_by_character(clip_groups)

    # 为每个角色组生成不重叠的音轨
    audio_tracks = flatten_chara_grps(character_groups)
    # 插入间隙
    for track in audio_tracks:
        track.clips = generate_gaps_between_clips(track.clips)

    return audio_tracks
