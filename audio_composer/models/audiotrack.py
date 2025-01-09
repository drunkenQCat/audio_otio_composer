from audio_composer.models.audioclip import AudioClip
from dataclasses import dataclass, field


@dataclass
class AudioTrack:
    character: str
    index: int
    clips: list[AudioClip] = field(default_factory=list)

    @property
    def track_name(self) -> str:
        return f"{self.character}_{self.index}"

    def __repr__(self):
        return f"\nAudioTrack(character='{self.character}', index={self.index}, clips=\n{self.clips}\n)"


@dataclass
class CharacterGroup:
    character: str
    tracks: list[AudioTrack] = field(default_factory=list)

    def __repr__(self):
        return f"\nCharacterGroup(character='{self.character}', tracks={self.tracks}')"
