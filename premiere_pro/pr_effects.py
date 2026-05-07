"""Premiere Pro OTIO effect generation helpers.

Reference: PR_OTIO_Metadata_Reference.md (from Pr_Ice_Test.otio)
"""

from opentimelineio.schema import Clip, Effect, Track


def _make_start_value(fps: float, value) -> dict:
    """构建 StartValue 结构，Position.rate 使用传入的 fps。"""
    return {
        "Position": {
            "rate": fps,
            "value": -9000000.0,
        },
        "Value": value,
    }


def _make_keyframe_param(name: str, param_id: int) -> dict:
    """构建 Keyframe 类型的参数（用于 Track effects）。"""
    return {
        "DisplayName": name,
        "ID": param_id,
        "Keyframes": [],
    }


def _make_startvalue_param(name: str, param_id: int, value, fps: float) -> dict:
    """构建 StartValue 类型的参数（用于 Clip effects）。"""
    return {
        "DisplayName": name,
        "ID": param_id,
        "StartValue": _make_start_value(fps, value),
    }


# ---------------------------------------------------------------------------
# Track-level effects
# ---------------------------------------------------------------------------

def add_pr_track_effects(track: Track, fps: float) -> None:
    """向音频轨道添加 PR 格式的 AudioFader 和 PanProcessor 效果。

    PR 参考: 每条音频轨道均有:
        Effect[0]: AudioFader (Volume + Mute)
        Effect[1]: PanProcessor (Balance)
    """
    # --- AudioFader ---
    fx_af = Effect()
    fx_af.effect_name = "轨道"
    fx_af.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": False,
        "MatchName": "AudioFader",
        "Parameters": [
            _make_keyframe_param("Volume", 0),
            _make_keyframe_param("Mute", 1),
        ],
    }
    fx_af.enabled = True
    track.effects.append(fx_af)

    # --- PanProcessor (Track) ---
    fx_pp = Effect()
    fx_pp.effect_name = "Panner"
    fx_pp.name = "Panner"
    fx_pp.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": False,
        "MatchName": "PanProcessor",
        "Parameters": [
            _make_keyframe_param("Balance", 0),
        ],
    }
    fx_pp.enabled = True
    track.effects.append(fx_pp)


# ---------------------------------------------------------------------------
# Clip-level effects
# ---------------------------------------------------------------------------

def add_pr_mono_clip_effects(clip: Clip, fps: float) -> None:
    """向单声道音频 Clip 添加 PR 格式效果。

    PR 参考:
        Effect[0]: Internal Volume Mono (静音 + 级别)
        Effect[1]: PanProcessor (Pan)
    """
    # --- Internal Volume Mono ---
    fx_vol = Effect()
    fx_vol.effect_name = "音量"
    fx_vol.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": True,
        "MatchName": "Internal Volume Mono",
        "Parameters": [
            _make_keyframe_param("静音", 0),
            _make_keyframe_param("级别", 1),
        ],
    }
    fx_vol.enabled = True
    clip.effects.append(fx_vol)

    # --- PanProcessor (Clip) ---
    fx_pp = Effect()
    fx_pp.effect_name = "Panner"
    fx_pp.name = "Panner"
    fx_pp.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": False,
        "MatchName": "PanProcessor",
        "Parameters": [
            _make_keyframe_param("Pan", 0),
        ],
    }
    fx_pp.enabled = True
    clip.effects.append(fx_pp)


def add_pr_stereo_clip_effects(clip: Clip, fps: float) -> None:
    """向立体声音频 Clip 添加 PR 格式效果。

    PR 参考:
        Effect[0]: Internal Volume Stereo (静音 + 级别)
        Effect[1]: Internal Channel Volume Stereo (旁路 + 左侧 + 右侧 + 30个空DisplayName)
        Effect[2]: PanProcessor (平衡)
    """
    # --- Internal Volume Stereo ---
    fx_vol = Effect()
    fx_vol.effect_name = "音量"
    fx_vol.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": True,
        "MatchName": "Internal Volume Stereo",
        "Parameters": [
            _make_keyframe_param("静音", 0),
            _make_keyframe_param("级别", 1),
        ],
    }
    fx_vol.enabled = True
    clip.effects.append(fx_vol)

    # --- Internal Channel Volume Stereo ---
    fx_ch = Effect()
    fx_ch.effect_name = "通道音量"
    ch_params = [
        _make_keyframe_param("旁路", 0),
        _make_keyframe_param("左侧", 1),
        _make_keyframe_param("右侧", 2),
    ]
    for i in range(3, 33):
        ch_params.append(_make_keyframe_param("", i))
    fx_ch.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": True,
        "MatchName": "Internal Channel Volume Stereo",
        "Parameters": ch_params,
    }
    fx_ch.enabled = True
    clip.effects.append(fx_ch)

    # --- PanProcessor (Clip Stereo) ---
    fx_pp = Effect()
    fx_pp.effect_name = "Panner"
    fx_pp.name = "Panner"
    fx_pp.metadata["PremierePro_OTIO"] = {
        "IsIntrinsic": False,
        "MatchName": "PanProcessor",
        "Parameters": [
            _make_keyframe_param("平衡", 0),
        ],
    }
    fx_pp.enabled = True
    clip.effects.append(fx_pp)


def add_pr_clip_effects(clip: Clip, channel_count: int, fps: float) -> None:
    """根据声道数，向 Clip 添加对应的 PR 格式效果。

    Args:
        clip: OTIO Clip 对象。
        channel_count: 声道数 (1 → Mono effects, ≥2 → Stereo effects)。
        fps: 帧率。
    """
    if channel_count == 1:
        add_pr_mono_clip_effects(clip, fps)
    else:
        add_pr_stereo_clip_effects(clip, fps)
