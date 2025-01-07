import unittest
from pathlib import Path
from models.audioclip import AudioClip
from models.audiotrack import AudioTrack, CharacterGroup
from audio_to_timeline import (
    get_audio_clips,
    group_clips_by_character,
    organize_tracks_by_character,
    generate_no_overlap_tracks,
    generate_gap,
    generate_gaps_between_clips,
    flatten_chara_grps,
    audio_to_timeline,
)


class TestAudioToTimeline(unittest.TestCase):
    def setUp(self):
        # 设置测试用的音频剪辑
        self.clip1 = AudioClip(audio_file="test_data/audio1.wav", frame_rate=24)
        self.clip2 = AudioClip(audio_file="test_data/audio2.wav", frame_rate=24)
        self.clip3 = AudioClip(audio_file="test_data/audio3.wav", frame_rate=24)
        self.clip4 = AudioClip(audio_file="test_data/audio4.wav", frame_rate=24)
        self.clip5 = AudioClip(audio_file="test_data/audio5.wav", frame_rate=24)
        self.clip6 = AudioClip(audio_file="test_data/audio6.wav", frame_rate=24)
        self.clip7 = AudioClip(audio_file="test_data/audio7.wav", frame_rate=24)
        self.clip8 = AudioClip(audio_file="test_data/audio8.wav", frame_rate=24)
        self.clip9 = AudioClip(audio_file="test_data/audio9.wav", frame_rate=24)

        self.clips = [
            self.clip1,
            self.clip2,
            self.clip3,
            self.clip4,
            self.clip5,
            self.clip6,
            self.clip7,
            self.clip8,
            self.clip9,
        ]

    def test_group_clips_by_character(self):
        groups = group_clips_by_character(self.clips)
        expected = [
            (
                "Alice",
                [
                    self.clip1,
                    self.clip2,
                    self.clip3,
                    self.clip4,
                    self.clip5,
                    self.clip6,
                ],
            ),
            (
                "Bob",
                [
                    self.clip7,
                    self.clip8,
                    self.clip9,
                ],
            ),
        ]
        self.assertEqual(len(groups), 2)
        self.assertIn(expected[0], groups)
        self.assertIn(expected[1], groups)

    def test_generate_no_overlap_tracks(self):
        groups = group_clips_by_character(self.clips)
        character_groups = organize_tracks_by_character(groups)
        alice_group = next(
            (group for group in character_groups if group.character == "Alice"), None
        )
        self.assertIsNotNone(alice_group)
        if alice_group is None:
            return
        self.assertEqual(len(alice_group.tracks), 3)  # 因为clip1和clip3有重叠
        for track in alice_group.tracks:
            start_times = [clip.start_offset for clip in track.clips]
            end_times = [clip.end_offset for clip in track.clips]
            start_end_list = zip(start_times, end_times)
            start_end_list = list(start_end_list)
            self.assertFalse(self.is_any_clip_overlap(start_end_list))

    def is_any_clip_overlap(self, start_end_list: list[tuple[float, float]]) -> bool:
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

    def test_generate_gap(self):
        gap_duration = 2.5
        gap = generate_gap(gap_duration)
        self.assertEqual(2.5, gap.duration)
        self.assertEqual("gap", gap.character)

    def test_generate_gaps_between_clips(self):
        clips_with_gaps = audio_to_timeline(self.clips)[0].clips
        # 应包含间隙和原始剪辑
        self.assertEqual(4, len(clips_with_gaps))
        self.assertEqual("gap", clips_with_gaps[0].character)
        self.assertEqual(0, clips_with_gaps[0].duration)
        self.assertEqual("Alice", clips_with_gaps[1].character)
        self.assertEqual("gap", clips_with_gaps[2].character)
        self.assertEqual(1, clips_with_gaps[2].duration)
        self.assertEqual("Alice", clips_with_gaps[3].character)

    def test_audio_to_timeline(self):
        audio_tracks = audio_to_timeline(self.clips)
        # 根据设置，应该有2轨Alice和1轨Bob
        self.assertEqual(4, len(audio_tracks))
        alice_tracks = [track for track in audio_tracks if track.character == "Alice"]
        bob_tracks = [track for track in audio_tracks if track.character == "Bob"]
        self.assertEqual(3, len(alice_tracks))
        self.assertEqual(1, len(bob_tracks))


if __name__ == "__main__":
    unittest.main()
