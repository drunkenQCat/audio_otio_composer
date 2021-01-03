from __future__ import annotations
from opentimelineio._opentime import RationalTime
from opentimelineio._opentime import TimeRange
from opentimelineio._opentime import TimeTransform
from opentimelineio._opentime import duration_from_start_end_time
from opentimelineio._opentime import duration_from_start_end_time_inclusive
from opentimelineio._opentime import from_frames
from opentimelineio._opentime import from_seconds
from opentimelineio._opentime import from_time_string
from opentimelineio._opentime import from_timecode
from opentimelineio._opentime import range_from_start_end_time
from opentimelineio._opentime import range_from_start_end_time_inclusive
__all__: list = ['RationalTime', 'TimeRange', 'TimeTransform', 'from_frames', 'from_timecode', 'from_time_string', 'from_seconds', 'to_timecode', 'to_nearest_timecode', 'to_frames', 'to_seconds', 'to_time_string', 'range_from_start_end_time', 'range_from_start_end_time_inclusive', 'duration_from_start_end_time', 'duration_from_start_end_time_inclusive']
def to_frames(rt, rate = None):
    """
    Turn a :class:`~RationalTime` into a frame number.
    """
def to_nearest_timecode(rt, rate = None, drop_frame = None):
    """
    Convert a :class:`~RationalTime` into a timecode string.
    """
def to_seconds(rt):
    """
    Convert a :class:`~RationalTime` into float seconds
    """
def to_time_string(rt):
    """
    
        Convert this timecode to time as used by ffmpeg, formatted as
        ``hh:mm:ss`` where ss is an integer or decimal number.
        
    """
def to_timecode(rt, rate = None, drop_frame = None):
    """
    Convert a :class:`~RationalTime` into a timecode string.
    """
