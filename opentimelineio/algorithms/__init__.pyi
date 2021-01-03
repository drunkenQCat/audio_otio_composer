"""
Algorithms for OTIO objects.
"""
from __future__ import annotations
from opentimelineio._otio import flatten_stack
from opentimelineio.algorithms.filter import filtered_composition
from opentimelineio.algorithms.filter import filtered_with_sequence_context
from opentimelineio.algorithms.stack_algo import top_clip_at_time
from opentimelineio.algorithms.timeline_algo import timeline_trimmed_to_range
from opentimelineio.algorithms.track_algo import track_trimmed_to_range
from opentimelineio.algorithms.track_algo import track_with_expanded_transitions
from . import filter
from . import stack_algo
from . import timeline_algo
from . import track_algo
__all__ = ['filter', 'filtered_composition', 'filtered_with_sequence_context', 'flatten_stack', 'stack_algo', 'timeline_algo', 'timeline_trimmed_to_range', 'top_clip_at_time', 'track_algo', 'track_trimmed_to_range', 'track_with_expanded_transitions']
