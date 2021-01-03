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
from opentimelineio._otio.Marker import Color as MarkerColor
from opentimelineio._otio import MissingReference
from opentimelineio._otio import SerializableCollection
from opentimelineio._otio import Stack
from opentimelineio._otio import TimeEffect
from opentimelineio._otio import Timeline
from opentimelineio._otio import Track
from opentimelineio._otio.Track import Kind as TrackKind
from opentimelineio._otio.Track import NeighborGapPolicy
from opentimelineio._otio import Transition
from opentimelineio._otio.Transition import Type as TransitionTypes
from opentimelineio._otio import V2d
from opentimelineio.schema.schemadef import SchemaDef
from . import box2d
from . import clip
from . import effect
from . import external_reference
from . import generator_reference
from . import image_sequence_reference
from . import marker
from . import schemadef
from . import serializable_collection
from . import timeline
from . import transition
from . import v2d
__all__: list = ['Box2d', 'Clip', 'Effect', 'TimeEffect', 'LinearTimeWarp', 'ExternalReference', 'FreezeFrame', 'Gap', 'GeneratorReference', 'ImageSequenceReference', 'Marker', 'MissingReference', 'SerializableCollection', 'Stack', 'Timeline', 'Transition', 'SchemaDef', 'timeline_from_clips', 'V2d']
def timeline_from_clips(clips):
    """
    Convenience for making a single track timeline from a list of clips.
    """
