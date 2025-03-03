from opentimelineio.opentime import TimeRange, RationalTime
from opentimelineio.schema import Clip, ExternalReference, Gap
from pathlib import Path
import wavinfo

from davinci_resolve.metadata_manager.fx_generator import add_default_afxs
from utils.logger import logger


class AudioClip:
    audio_path: str
    character: str = "character A"
    start_offset: float = 0.0
    duration: float = 0.0
    frame_rate: float = 24.0

    def __init__(self, audio_file: str, rate: float = 24.0):
        self.audio_range = TimeRange()
        self.clip: Clip | Gap = Clip()

        audio_path = Path(audio_file)
        self.audio_path = str(audio_path.absolute())
        self.clip.name = audio_path.name

        self.frame_rate = rate

        # 获取wav元数据
        info = wavinfo.WavInfoReader(
            audio_file, info_encoding="utf8", bext_encoding="utf8"
        )
        if not info or not info.fmt or not info.data:
            logger.warn("Warning: please check the wav audio data")
            return
        if not info.bext or not info.info:
            logger.warn("Warning: please check the wav metadata")
            return

        # 获取偏移时间
        sample_rate = info.fmt.sample_rate
        offset_time_in_sample_count = info.bext.time_reference
        self.start_offset = offset_time_in_sample_count / sample_rate

        # 获取音频时长
        self.duration = info.data.frame_count / sample_rate
        self.audio_range = TimeRange(
            RationalTime(0, self.frame_rate),
            RationalTime().from_seconds(self.duration, self.frame_rate),
        )

        # 获取通道数
        channel_count = info.fmt.channel_count
        self.clip.metadata["Resolve_OTIO"] = self.generate_davinci_channel_metadata(
            channel_count
        )

        # 获取角色名
        self.character = "character A" if not info.info.artist else info.info.artist

        # 与文件链接
        external_range = TimeRange(
            RationalTime().from_seconds(self.start_offset, self.frame_rate),
            RationalTime().from_seconds(self.duration, self.frame_rate),
        )
        self.clip.media_reference = ExternalReference(
            target_url=self.audio_path, available_range=external_range
        )
        self.clip.media_reference.name = audio_path.name
        self.clip.source_range = self.audio_range

        # 添加默认音频效果
        add_default_afxs(self.clip)

    @staticmethod
    def generate_davinci_channel_metadata(channel_count: int) -> dict[str, list[dict]]:
        channel_info = []
        for id in range(channel_count):
            current_channel = {"Source Channel ID": id, "Source Track ID": id}
            channel_info.append(current_channel)

        return {"Channels": channel_info}

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
    def __init__(self, duration: float, rate: float = 24.0):
        self.duration = duration

        self.frame_rate = rate

        gap = Gap()
        gap.source_range = TimeRange(
            duration=RationalTime().from_seconds(duration, self.frame_rate)
        )
        gap.name = "black"
        self.clip = gap

        self.character = "gap"

    def __repr__(self):
        return f"\nGap(duration={self.duration})"
