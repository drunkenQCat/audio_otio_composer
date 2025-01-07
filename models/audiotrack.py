from models.audioclip import AudioClip


class AudioTrack:
    def __init__(
        self,
        character: str,
        index: int,
        clips: list[AudioClip] = [],
    ) -> None:
        self.character = character
        self.index = index
        self.clips = clips

    @property
    def track_name(self) -> str:
        return f"{self.character}_{self.index}"


class CharacterGroup:
    def __init__(
        self,
        character: str,
        tracks: list[AudioTrack] = [],
    ) -> None:
        self.character = character
        self.tracks = tracks
