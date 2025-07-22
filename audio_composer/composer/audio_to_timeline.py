from pathlib import Path
import os

from audio_composer.composer.scanline_composer import generate_no_overlap_tracks
from audio_composer.models.audioclip import AudioClip, AudioGap
from audio_composer.models.audiotrack import AudioTrack, CharacterGroup


def safe_path(path: Path) -> str:
    """将 Path 转成带windows 标准长路径前缀的绝对路径字符串"""
    if os.name == "nt":
        abs_path = path.resolve()
        return f"\\\\?\\{abs_path}"
    else:
        return path.as_posix()


def get_audio_clips(folder: str, fps: float = 24.0) -> list[AudioClip]:
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
        clip = AudioClip(audio_file=safe_path(audio_file), rate=fps)
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
    clip_groups: list[tuple[str, list[AudioClip]]],
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


def merge_tracks(tracks: list[AudioTrack], threshold: float = 1.0) -> list[AudioTrack]:
    """
    合并轨道，将空隙较小的轨道合并到一个轨道。

    参数:
        tracks (list[AudioTrack]): 音轨列表。
        threshold (float): 判断是否可以合并的空隙阈值（单位：时间长度）。

    返回:
        list[AudioTrack]: 合并后的音轨列表。
    """
    # 按轨道结束时间排序
    tracks.sort(
        key=lambda track: track.clips[-1].end_offset if track.clips else float("inf")
    )

    merged_tracks = []
    current_track = tracks[0]

    for i in range(1, len(tracks)):
        last_clip_end_time = current_track.clips[-1].end_offset
        first_clip_start_time = tracks[i].clips[0].start_offset

        # 如果轨道之间的空隙小于阈值，则尝试合并
        if first_clip_start_time - last_clip_end_time <= threshold:
            # 将轨道i的所有片段加到当前轨道
            current_track.clips.extend(tracks[i].clips)
        else:
            # 否则，保留当前轨道，创建新的轨道
            merged_tracks.append(current_track)
            current_track = tracks[i]

    # 最后添加剩下的轨道
    merged_tracks.append(current_track)

    return merged_tracks


def generate_gap(duration: float, fps: float = 24.0) -> AudioGap:
    """
    生成一个音频间隙。

    参数:
        duration (float): 间隙的持续时间（秒）。

    返回:
        AudioClip: 生成的间隙音频剪辑。
    """
    gap = AudioGap(duration=duration, rate=fps)

    return gap


def generate_gaps_between_clips(
    clips: list[AudioClip], fps: float = 24.0
) -> list[AudioClip]:
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
        if gap_duration == 0:
            continue
        gap = generate_gap(gap_duration, fps)

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


def audio_to_tracks(clips: list[AudioClip], fps: float = 24.0) -> list[AudioTrack]:
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
        track.clips = generate_gaps_between_clips(track.clips, fps)

    return audio_tracks
