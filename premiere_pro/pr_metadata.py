"""Premiere Pro OTIO metadata generation helpers.

Reference: PR_OTIO_Metadata_Reference.md (from Pr_Ice_Test.otio)
"""


def make_timeline_metadata() -> dict:
    """生成 Timeline 级别的 PremierePro_OTIO metadata。

    PR 参考:
        PremierePro_OTIO:
            MetadataVersion: "1.0"
    """
    return {
        "PremierePro_OTIO": {
            "MetadataVersion": "1.0",
        }
    }


def make_stack_metadata(
    fps: float = 25.0,
    video_width: int = 1920,
    video_height: int = 1080,
    audio_frame_rate: float = 48000.0,
) -> dict:
    """生成 Stack (Tracks) 级别的 PremierePro_OTIO metadata。

    PR 参考:
        PremierePro_OTIO:
            AudioFrameRate: 48000.0
            PixelAspectRatio: {denominator: 1.0, numerator: 1.0}
            VideoFrameRate: 25.0
            VideoResolution: {height: 1080, width: 1920}
    """
    return {
        "PremierePro_OTIO": {
            "AudioFrameRate": audio_frame_rate,
            "PixelAspectRatio": {
                "denominator": 1.0,
                "numerator": 1.0,
            },
            "VideoFrameRate": fps,
            "VideoResolution": {
                "height": video_height,
                "width": video_width,
            },
        }
    }


def make_audio_track_metadata(channel_count: int) -> dict:
    """生成音频轨道级别的 PremierePro_OTIO metadata。

    PR 参考:
        PremierePro_OTIO:
            AudioChannels:
                ChannelType: "Stereo" | "Mono"
                NumberOfChannels: 2 | 1

    Args:
        channel_count: 声道数 (1=Mono, 2+=Stereo)。
    """
    channel_type = "Mono" if channel_count == 1 else "Stereo"
    return {
        "PremierePro_OTIO": {
            "AudioChannels": {
                "ChannelType": channel_type,
                "NumberOfChannels": min(channel_count, 2),
            }
        }
    }


def make_clip_metadata(channel_count: int) -> dict:
    """生成 Clip 级别的 PremierePro_OTIO metadata。

    PR 参考:
        PremierePro_OTIO:
            AudioChannels:
                ChannelType: "Mono" | "Stereo"
                SecondaryAssignments:
                    - SecondaryChannelIndex: 0
                    - SecondaryChannelIndex: 1  (仅 Stereo)
            OriginalChannelGroupIndex: 0
            SourceClipIndex: 0

    Args:
        channel_count: 声道数。
    """
    channel_type = "Mono" if channel_count == 1 else "Stereo"
    secondary_assignments = [
        {"SecondaryChannelIndex": i}
        for i in range(min(channel_count, 2))
    ]
    return {
        "PremierePro_OTIO": {
            "AudioChannels": {
                "ChannelType": channel_type,
                "SecondaryAssignments": secondary_assignments,
            },
            "OriginalChannelGroupIndex": 0,
            "SourceClipIndex": 0,
        }
    }
