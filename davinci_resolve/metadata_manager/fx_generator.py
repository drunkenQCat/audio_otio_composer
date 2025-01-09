from opentimelineio._otio import Clip
from opentimelineio.schema import Effect
from davinci_resolve.models.resolve_fx import default_afxs, default_vfxs


def add_default_afxs(clip: Clip) -> None:
    for effect in default_afxs.effects:
        fx = Effect()
        fx.effect_name = effect.effect_name
        fx.metadata["Resolve_OTIO"] = effect.metadata.resolve_otio.model_dump(
            by_alias=True
        )
        clip.effects.append(fx)


def add_default_vfxs(clip: Clip) -> None:
    for effect in default_vfxs.effects:
        fx = Effect()
        fx.effect_name = effect.effect_name
        fx.metadata["Resolve_OTIO"] = effect.metadata.resolve_otio.model_dump(
            by_alias=True
        )
        clip.effects.append(fx)
