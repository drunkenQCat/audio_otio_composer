import pytest
from models.audioclip import AudioClip
from audio_to_timeline import (
    get_audio_clips,
    group_clips_by_character,
    organize_tracks_by_character,
    generate_gap,
    audio_to_tracks,
)


@pytest.fixture
def clips():
    # 设置测试用的音频剪辑
    return [
        AudioClip(audio_file="test_data/audio1.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio2.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio3.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio4.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio5.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio6.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio7.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio8.wav", frame_rate=24),
        AudioClip(audio_file="test_data/audio9.wav", frame_rate=24),
    ]


def is_any_clip_overlap(start_end_list):
    # Convert the start_end_list to a sorted list based on the start time
    sorted_clips = sorted(start_end_list, key=lambda x: x[0])

    # Check for overlaps
    for i in range(1, len(sorted_clips)):
        prev_clip_end = sorted_clips[i - 1][1]
        curr_clip_start = sorted_clips[i][0]

        # If the start of the current clip is before the end of the previous clip, it's an overlap
        if curr_clip_start < prev_clip_end:
            return True

    # No overlaps found
    return False


def test_get_audio_clips():
    clips = get_audio_clips("test_data")
    assert len(clips) == 9


def test_group_clips_by_character(clips):
    groups = group_clips_by_character(clips)
    expected = [
        (
            "Alice",
            clips[:6],
        ),
        (
            "Bob",
            clips[6:],
        ),
    ]
    assert len(groups) == 2
    assert expected[0] in groups
    assert expected[1] in groups


def test_generate_no_overlap_tracks(clips):
    groups = group_clips_by_character(clips)
    character_groups = organize_tracks_by_character(groups)
    alice_group = next(
        (group for group in character_groups if group.character == "Alice"), None
    )
    assert alice_group is not None
    if alice_group is None:
        return
    assert len(alice_group.tracks) == 3  # 因为clip1和clip3有重叠
    for track in alice_group.tracks:
        start_times = [clip.start_offset for clip in track.clips]
        end_times = [clip.end_offset for clip in track.clips]
        start_end_list = list(zip(start_times, end_times))
        assert not is_any_clip_overlap(start_end_list)


def test_generate_gap():
    gap_duration = 2.5
    gap = generate_gap(gap_duration)
    assert gap.duration == 2.5
    assert gap.character == "gap"


def test_generate_gaps_between_clips(clips):
    clips_with_gaps = audio_to_tracks(clips)[0].clips
    # 应包含间隙和原始剪辑
    assert len(clips_with_gaps) == 4
    assert clips_with_gaps[0].character == "gap"
    assert clips_with_gaps[0].duration == 0
    assert clips_with_gaps[1].character == "Alice"
    assert clips_with_gaps[2].character == "gap"
    assert clips_with_gaps[2].duration == 2.0
    assert clips_with_gaps[3].character == "Alice"


def test_audio_to_timeline(clips):
    audio_tracks = audio_to_tracks(clips)
    # 根据设置，应该有2轨Alice和1轨Bob
    assert len(audio_tracks) == 4
    alice_tracks = [track for track in audio_tracks if track.character == "Alice"]
    bob_tracks = [track for track in audio_tracks if track.character == "Bob"]
    assert len(alice_tracks) == 3
    assert len(bob_tracks) == 1
