"""
Algorithms for timeline objects.
"""
from __future__ import annotations
import copy as copy
from opentimelineio.algorithms import track_algo
__all__ = ['copy', 'timeline_trimmed_to_range', 'track_algo']
def timeline_trimmed_to_range(in_timeline, trim_range):
    """
    
        Returns a new timeline that is a copy of the in_timeline, but with items
        outside the trim_range removed and items on the ends trimmed to the
        trim_range.
    
        .. note:: the timeline is never expanded, only shortened.
    
        Please note that you could do nearly the same thing non-destructively by
        just setting the :py:class:`.Track`'s source_range but sometimes you want to
        really cut away the stuff outside and that's what this function is meant for.
    
        :param Timeline in_timeline: Timeline to trim
        :param TimeRange trim_range:
        :returnd: New trimmed timeline
        :rtype: Timeline
        
    """
