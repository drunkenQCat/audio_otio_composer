from pydantic import BaseModel, Field
import json
from typing import List, Dict, Union, Optional


class KeyFrame(BaseModel):
    value: Union[float, List[float]] = Field(..., alias="Value")
    variant_type: str = Field(..., alias="Variant Type")


class Parameter(BaseModel):
    default_parameter_value: Union[int, float, List[float]] = Field(
        ..., alias="Default Parameter Value"
    )
    parameter_id: str = Field(..., alias="Parameter ID")
    parameter_value: Union[
        int,
        float,
        List[float],
    ] = Field(..., alias="Parameter Value")
    variant_type: str = Field(..., alias="Variant Type")
    key_frames: Optional[Dict[str, KeyFrame]] = Field(
        default_factory=dict, alias="Key Frames"
    )
    max_value: Optional[float] = Field(default=None, alias="maxValue")
    min_value: Optional[float] = Field(default=None, alias="minValue")


class ResolveOTIO(BaseModel):
    effect_name: str = Field(..., alias="Effect Name")
    enabled: bool = Field(..., alias="Enabled")
    name: str = Field(..., alias="Name")
    parameters: List[Parameter] = Field(default_factory=list, alias="Parameters")
    fx_type: int = Field(..., alias="Type")


class Metadata(BaseModel):
    resolve_otio: ResolveOTIO = Field(..., alias="Resolve_OTIO")


class Effect(BaseModel):
    otio_schema: str = Field(..., alias="OTIO_SCHEMA")
    metadata: Metadata
    name: str = ""
    effect_name: str = Field(..., alias="effect_name")


class EffectList(BaseModel):
    effects: List[Effect]


# 模块级变量，用于缓存默认音频效果
default_audio_fxs = None
default_video_fxs = None


# 加载默认音频效果数据
def load_default_audio_fxs() -> EffectList:
    global default_audio_fxs
    if default_audio_fxs is None:
        with open(
            "davinci_resolve/default_data/audio_fxs.json", "r", encoding="utf-8"
        ) as file:
            json_data = json.load(file)
        default_audio_fxs = EffectList.model_validate(json_data)
    return default_audio_fxs


# 加载默认视频效果数据
def load_default_video_fxs() -> EffectList:
    global default_video_fxs
    if default_video_fxs is None:
        with open(
            "davinci_resolve/default_data/video_fxs.json", "r", encoding="utf-8"
        ) as file:
            json_data = json.load(file)
        default_video_fxs = EffectList.model_validate(json_data)
    return default_video_fxs


# 初始化并获取默认音频效果
default_afxs = load_default_audio_fxs()
default_vfxs = load_default_video_fxs()
