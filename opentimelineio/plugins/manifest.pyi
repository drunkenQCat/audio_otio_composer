"""
OTIO Python Plugin Manifest system: locates plugins to OTIO.
"""
from __future__ import annotations
from importlib import metadata
from importlib import resources
import inspect as inspect
import logging as logging
import opentimelineio._otio
from opentimelineio import core
from opentimelineio import exceptions
import os as os
from pathlib import Path
import typing
__all__ = ['ActiveManifest', 'Manifest', 'OTIO_PLUGIN_TYPES', 'Path', 'core', 'exceptions', 'inspect', 'load_manifest', 'logging', 'manifest_from_file', 'manifest_from_string', 'metadata', 'os', 'plugin_entry_points', 'resources']
class Manifest(opentimelineio._otio.SerializableObject):
    """
    Defines an OTIO plugin Manifest.
    
        This is considered an internal OTIO implementation detail.
    
        A manifest tracks a collection of plugins and enables finding them by name
        or other features (in the case of adapters, what file suffixes they
        advertise support for).
    
        For more information, consult the documenation.
        
    """
    _serializable_label: typing.ClassVar[str] = 'PluginManifest.1'
    def __init__(self, *args, **kwargs):
        ...
    def _update_plugin_source(self, path):
        """
        Set the source file path for the manifest.
        """
    def adapter_module_from_name(self, name):
        """
        Return the adapter module associated with a given adapter name.
        """
    def adapter_module_from_suffix(self, suffix):
        """
        Return the adapter module associated with a given file suffix.
        """
    def extend(self, another_manifest):
        """
        
                Aggregate another manifest's plugins into this one.
        
                During startup, OTIO will deserialize the individual manifest JSON files
                and use this function to concatenate them together.
                
        """
    def from_filepath(self, suffix):
        """
        Return the adapter object associated with a given file suffix.
        """
    def from_name(self, name, kind_list = 'adapters'):
        """
        Return the plugin object associated with a given plugin name.
        """
    def schemadef_module_from_name(self, name):
        """
        Return the schemadef module associated with a given schemadef name.
        """
    @property
    def adapters(self):
        """
        Adapters this manifest describes.
        """
    @adapters.setter
    def adapters(self, val):
        ...
    @property
    def hook_scripts(self):
        """
        Scripts that can be attached to hooks.
        """
    @hook_scripts.setter
    def hook_scripts(self, val):
        ...
    @property
    def hooks(self):
        """
        Hooks that hooks scripts can be attached to.
        """
    @hooks.setter
    def hooks(self, val):
        ...
    @property
    def media_linkers(self):
        """
        Media Linkers this manifest describes.
        """
    @media_linkers.setter
    def media_linkers(self, val):
        ...
    @property
    def schemadefs(self):
        """
        Schemadefs this manifest describes.
        """
    @schemadefs.setter
    def schemadefs(self, val):
        ...
    @property
    def version_manifests(self):
        """
        Sets of versions to downgrade schemas to.
        """
    @version_manifests.setter
    def version_manifests(self, val):
        ...
def ActiveManifest(force_reload = False):
    """
    Return the fully resolved plugin manifest.
    """
def load_manifest():
    """
    Walk the plugin manifest discovery systems and accumulate manifests.
    
        The order of loading (and precedence) is:
    
           1. Manifests specified via the :term:`OTIO_PLUGIN_MANIFEST_PATH` variable
           2. Entrypoint based plugin manifests
           3. Builtin plugin manifest
        
    """
def manifest_from_file(filepath):
    """
    Read the .json file at filepath into a :py:class:`Manifest` object.
    """
def manifest_from_string(input_string):
    """
    Deserialize the json string into a manifest object.
    """
def plugin_entry_points():
    """
    Returns the list of entry points for all available OpenTimelineIO
        plugins.
        
    """
OTIO_PLUGIN_TYPES: list = ['adapters', 'media_linkers', 'schemadefs', 'hook_scripts', 'hooks', 'version_manifests']
_MANIFEST = None
