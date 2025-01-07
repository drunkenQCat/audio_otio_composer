from models.audioclip import AudioClip
from dataclasses import dataclass, field


@dataclass
class AudioTrack:
    character: str
    index: int
    clips: list[AudioClip] = field(default_factory=list)

    @property
    def track_name(self) -> str:
        return f"{self.character}_{self.index}"


@dataclass
class CharacterGroup:
    character: str
    tracks: list[AudioTrack] = field(default_factory=list)
