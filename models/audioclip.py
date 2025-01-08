from opentimelineio.opentime import TimeRange, RationalTime
from opentimelineio.schema import Clip, ExternalReference, Gap
from pathlib import Path
import wavinfo


class AudioClip:
    audio_path: str
    frame_rate: float = 24
    character: str = ""
    start_offset: float = 0.0
    duration: float = 0.0

    def __init__(self, audio_file: str, frame_rate: float = 24):
        self.audio_range = TimeRange()
        self.clip: Clip | Gap = Clip()

        audio_path = Path(audio_file)
        self.audio_path = str(audio_path.absolute())
        self.clip.name = audio_path.name

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
            target_url=self.audio_path, available_range=self.audio_range
        )
        self.clip.source_range = self.audio_range

    @property
    def end_offset(self) -> float:
        return self.start_offset + self.duration

    def __lt__(self, other):
        return self.start_offset < other.start_offset

    def __repr__(self):
        return f"""
        AudioClip(
        audio_path='{self.audio_path}', 
        start_offset={self.start_offset}, duration={self.duration}, character='{self.character}'
        )"""


class AudioGap(AudioClip):
    def __init__(self, duration: float):
        self.duration = duration

        gap = Gap()
        gap.source_range = TimeRange(duration=RationalTime(duration, self.frame_rate))
        gap.name = "black"
        self.clip = gap

        self.character = "gap"

    def __repr__(self):
        return f"\nGap(duration={self.duration})"
