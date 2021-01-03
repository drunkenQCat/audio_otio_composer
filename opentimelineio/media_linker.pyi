"""

MediaLinker plugins fire after an adapter has read a file in order to
produce :class:`.MediaReference`\\s that point at valid, site specific media.

They expose a ``link_media_reference`` function with the signature:

.. py:function:: link_media_reference(in_clip: opentimelineio.schema.Clip) -> opentimelineio.core.MediaReference  # noqa
   :noindex:

   Example link_media_reference function.

To get context information, they can inspect the metadata on the clip and on
the media reference. The :meth:`.Composable.parent` method can be used to find the containing
track if metadata is stored there.
"""
from __future__ import annotations
import inspect as inspect
from opentimelineio import core
from opentimelineio import exceptions
from opentimelineio import plugins
import opentimelineio.plugins.python_plugin
import os as os
import typing
__all__ = ['MediaLinker', 'MediaLinkingPolicy', 'available_media_linker_names', 'core', 'default_media_linker', 'exceptions', 'from_name', 'inspect', 'linked_media_reference', 'os', 'plugins']
class MediaLinker(opentimelineio.plugins.python_plugin.PythonPlugin):
    _serializable_label: typing.ClassVar[str] = 'MediaLinker.1'
    def __init__(self, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def is_default_linker(self):
        ...
    def link_media_reference(self, in_clip, media_linker_argument_map = None):
        ...
    def plugin_info_map(self):
        """
        Adds extra adapter-specific information to call to the parent fn.
        """
class MediaLinkingPolicy:
    """
    Enum describing different media linker policies
    """
    DoNotLinkMedia: typing.ClassVar[str] = '__do_not_link_media'
    ForceDefaultLinker: typing.ClassVar[str] = '__default'
def available_media_linker_names():
    """
    Return a string list of the available media linker plugins.
    """
def default_media_linker():
    ...
def from_name(name):
    """
    Fetch the media linker object by the name of the adapter directly.
    """
def linked_media_reference(target_clip, media_linker_name = '__default', media_linker_argument_map = None):
    ...
