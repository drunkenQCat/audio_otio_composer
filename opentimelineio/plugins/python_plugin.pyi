"""
Base class for OTIO plugins that are exposed by manifests.
"""
from __future__ import annotations
import collections as collections
import copy as copy
import importlib as importlib
import inspect as inspect
import opentimelineio._otio
from opentimelineio import core
from opentimelineio import exceptions
from opentimelineio.plugins import manifest
import os as os
import typing
__all__ = ['PythonPlugin', 'collections', 'copy', 'core', 'exceptions', 'importlib', 'inspect', 'manifest', 'os', 'plugin_info_map']
class PythonPlugin(opentimelineio._otio.SerializableObject):
    """
    A class of plugin that is encoded in a python module, exposed via a
        manifest.
        
    """
    _serializable_label: typing.ClassVar[str] = 'PythonPlugin.1'
    def __init__(self, name = None, filepath = None):
        ...
    def _execute_function(self, func_name, **kwargs):
        """
        Execute func_name on this adapter with error checking.
        """
    def _imported_module(self, namespace):
        """
        Load the module this plugin points at.
        """
    def module(self):
        """
        Return the module object for this adapter. 
        """
    def module_abs_path(self):
        """
        Return an absolute path to the module implementing this adapter.
        """
    def plugin_info_map(self):
        """
        Returns a map with information about the plugin.
        """
    @property
    def filepath(self):
        """
        Absolute path or relative path to adapter module from location of json.
        """
    @filepath.setter
    def filepath(self, val):
        ...
    @property
    def name(self):
        """
        Adapter name.
        """
    @name.setter
    def name(self, val):
        ...
def plugin_info_map():
    ...
