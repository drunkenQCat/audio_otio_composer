from opentimelineio.opentime import TimeRange, RationalTime
from opentimelineio.schema import Clip, ExternalReference, Gap
from pathlib import Path
import wavinfo

from davinci_resolve.metadata_manager.fx_generator import add_default_afxs
from premiere_pro.pr_metadata import make_clip_metadata
from premiere_pro.pr_effects import add_pr_clip_effects
from utils.logger import logger

# Metadata 模式常量
MODE_MIX = "mix"
MODE_RESOLVE = "resolve"
MODE_PREMIERE = "premiere"


class AudioClip:
    audio_path: str
    character: str = "character A"
    start_offset: float = 0.0
    duration: float = 0.0
    frame_rate: float = 24.0
    channel_count: int = 1

    def __init__(
        self, audio_file: str, rate: float = 24.0, metadata_mode: str = MODE_MIX
    ):
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
            logger.warning("Warning: please check the wav audio data")
            return
        if not info.bext or not info.info:
            logger.warning("Warning: please check the wav metadata")
            return

        # 获取偏移时间
        sample_rate = info.fmt.sample_rate
        offset_time_in_sample_count = info.bext.time_reference
        self.start_offset = offset_time_in_sample_count / sample_rate

        # 获取音频时长
        self.duration = info.data.frame_count / sample_rate
        self.audio_range = TimeRange(
            RationalTime().from_seconds(self.start_offset, self.frame_rate),
            RationalTime().from_seconds(self.duration, self.frame_rate),
        )

        # 获取通道数
        self.channel_count = info.fmt.channel_count
        channel_count = self.channel_count

        # 根据 metadata_mode 添加 metadata
        if metadata_mode in (MODE_MIX, MODE_RESOLVE):
            self.clip.metadata["Resolve_OTIO"] = self.generate_davinci_channel_metadata(
                channel_count
            )
        if metadata_mode in (MODE_MIX, MODE_PREMIERE):
            self.clip.metadata.update(make_clip_metadata(channel_count))

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
        if metadata_mode in (MODE_MIX, MODE_RESOLVE):
            add_default_afxs(self.clip)
        if metadata_mode in (MODE_MIX, MODE_PREMIERE):
            add_pr_clip_effects(self.clip, channel_count, self.frame_rate)

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
        gap.name = ""
        self.clip = gap

        self.channel_count = 1
        self.character = "gap"

    def __repr__(self):
        return f"\nGap(duration={self.duration})"
