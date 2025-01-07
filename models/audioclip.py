from opentimelineio.opentime import TimeRange, RationalTime
from opentimelineio.schema import Clip, ExternalReference
import wavinfo


class AudioClip:
    frame_rate: float = 24
    audio_path: str
    start_offset: float = 0.0
    duration: float = 0.0
    audio_range: TimeRange = TimeRange()

    character: str

    clip: Clip = Clip()

    def __init__(self, audio_file: str, frame_rate: float = 24):
        self.audio_path = audio_file
        # 获取wav元数据
        info = wavinfo.WavInfoReader(audio_file)
        if not info or not info.fmt or not info.data:
            print("Warning: please check the wav audio data")
            return
        if not info.bext or not info.info:
            print("Warning: please check the wav metadata")
            return

        # 获取偏移时间
        sample_rate = info.fmt.sample_rate
        offset_time_in_sample_count = info.bext.time_reference
        self.start_offset = offset_time_in_sample_count / sample_rate

        # 获取音频时长
        self.duration = info.data.frame_count / sample_rate
        self.audio_range = TimeRange(
            RationalTime(0, frame_rate),
            RationalTime(self.duration, frame_rate),
        )

        # 获取角色名
        self.character = "" if not info.info.artist else info.info.artist

        # 初始化片段
        self.clip.media_reference = ExternalReference(
            target_url=audio_file, available_range=self.audio_range
        )
        self.clip.source_range = self.audio_range

    @property
    def end_offset(self) -> float:
        return self.start_offset + self.duration

    def __lt__(self, other):
        return self.start_offset < other.start_offset


class AudioGap(AudioClip):
    def __init__(self, duration: float):
        self.duration = duration
        self.character = "gap"
