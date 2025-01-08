"""
 Algorithms for stack objects. 
"""
from __future__ import annotations
from opentimelineio._otio import flatten_stack
from opentimelineio import opentime
from opentimelineio import schema
__all__ = ['flatten_stack', 'opentime', 'schema', 'top_clip_at_time']
def top_clip_at_time(in_stack, t):
    """
    Return the topmost visible child that overlaps with time ``t``.
    
        Example::
    
            tr1: G1, A, G2
            tr2: [B------]
            G1, and G2 are gaps, A and B are clips.
    
        If ``t`` is within ``A``, ``A`` will be returned. If ``t`` is within ``G1`` or
        ``G2``, ``B`` will be returned.
    
        :param Stack in_stack: Stack
        :param RationalTime t: Time
        :returns: Top clip
        :rtype: Clip
        
    """
