"""
User facing classes.
"""
from __future__ import annotations
from opentimelineio._otio import Box2d
from opentimelineio._otio import Clip
from opentimelineio._otio import Effect
from opentimelineio._otio import ExternalReference
from opentimelineio._otio import FreezeFrame
from opentimelineio._otio import Gap
from opentimelineio._otio import GeneratorReference
from opentimelineio._otio import ImageSequenceReference
from opentimelineio._otio import LinearTimeWarp
from opentimelineio._otio import Marker
from opentimelineio._otio import MissingReference
from opentimelineio._otio import SerializableCollection
from opentimelineio._otio import Stack
from opentimelineio._otio import TimeEffect
from opentimelineio._otio import Timeline
from opentimelineio._otio import Transition
from opentimelineio._otio import V2d
from opentimelineio.schema.schemadef import SchemaDef
__all__: list = ['Box2d', 'Clip', 'Effect', 'TimeEffect', 'LinearTimeWarp', 'ExternalReference', 'FreezeFrame', 'Gap', 'GeneratorReference', 'ImageSequenceReference', 'Marker', 'MissingReference', 'SerializableCollection', 'Stack', 'Timeline', 'Transition', 'SchemaDef', 'timeline_from_clips', 'V2d']
def timeline_from_clips(clips):
    """
    Convenience for making a single track timeline from a list of clips.
    """
