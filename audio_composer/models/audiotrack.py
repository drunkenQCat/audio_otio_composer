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

    def __getitem__(self, key: slice | float) -> list[AudioClip]:
        """Retrieve clips that overlap with the given time range or specific point."""
        if isinstance(key, slice):
            start_offset = key.start or 0
            end_offset = key.stop or float("inf")
            return [
                clip
                for clip in self.clips
                if clip.end_offset > start_offset and clip.start_offset < end_offset
            ]
        raise TypeError(f"Invalid key type: {type(key)}. Expected slice.")


@dataclass
class CharacterGroup:
    character: str
    tracks: list[AudioTrack] = field(default_factory=list)

    def __repr__(self):
        return f"\nCharacterGroup(character='{self.character}', tracks={self.tracks}')"
