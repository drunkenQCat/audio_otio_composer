"""
Plugin system for OTIO
"""
from __future__ import annotations
from opentimelineio.plugins.manifest import ActiveManifest
from opentimelineio.plugins.manifest import manifest_from_file
from opentimelineio.plugins.python_plugin import PythonPlugin
from opentimelineio.plugins.python_plugin import plugin_info_map
from . import manifest
from . import python_plugin
__all__ = ['ActiveManifest', 'PythonPlugin', 'manifest', 'manifest_from_file', 'plugin_info_map', 'python_plugin']
