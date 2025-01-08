from __future__ import annotations
import collections as collections
import copy as copy
from opentimelineio._otio import AnyDictionary
from opentimelineio._otio import AnyVector
from opentimelineio._otio import PyAny
from opentimelineio._otio import SerializableObject
import types as types
__all__ = ['AnyDictionary', 'AnyVector', 'PyAny', 'SUPPORTED_VALUE_TYPES', 'SerializableObject', 'add_method', 'collections', 'copy', 'deepcopy', 'types']
def __setattr__(self, key, value):
    ...
def _add_mutable_mapping_methods(mapClass):
    ...
def _add_mutable_sequence_methods(sequenceClass, conversion_func = None, side_effecting_insertions = False):
    ...
def _is_nonstring_sequence(v):
    ...
def _is_str(v):
    ...
def _value_to_any(value, ids = None):
    ...
def add_method(cls):
    ...
SUPPORTED_VALUE_TYPES: tuple = ('int', 'float', 'str', 'bool', 'list', 'dictionary', 'opentime.RationalTime', 'opentime.TimeRange', 'opentime.TimeTransform', 'opentimelineio.core.SerializableObject')
__copy__ = None
__deepcopy__ = None
_marker_: object  # value = <object object>
deepcopy = None
