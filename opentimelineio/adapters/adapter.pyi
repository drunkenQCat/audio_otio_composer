"""
Implementation of the OTIO internal `Adapter` system.

For information on writing adapters, please consult:
https://opentimelineio.readthedocs.io/en/latest/tutorials/write-an-adapter.html # noqa
"""
from __future__ import annotations
import collections as collections
import copy as copy
import inspect as inspect
from opentimelineio import core
from opentimelineio import hooks
from opentimelineio import media_linker
from opentimelineio import plugins
import opentimelineio.plugins.python_plugin
import typing
__all__ = ['Adapter', 'collections', 'copy', 'core', 'hooks', 'inspect', 'media_linker', 'plugins']
class Adapter(opentimelineio.plugins.python_plugin.PythonPlugin):
    """
    Adapters convert between OTIO and other formats.
    
        Note that this class is not subclassed by adapters. Rather, an adapter is
        a python module that implements at least one of the following functions:
    
        .. code-block:: python
    
            write_to_string(input_otio)
            write_to_file(input_otio, filepath) (optionally inferred)
            read_from_string(input_str)
            read_from_file(filepath) (optionally inferred)
    
        ...as well as a small json file that advertises the features of the adapter
        to OTIO.  This class serves as the wrapper around these modules internal
        to OTIO.  You should not need to extend this class to create new adapters
        for OTIO.
    
        For more information: https://opentimelineio.readthedocs.io/en/latest/tutorials/write-an-adapter.html. # noqa
        
    """
    _serializable_label: typing.ClassVar[str] = 'Adapter.1'
    def __init__(self, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def has_feature(self, feature_string):
        """
        
                return true if adapter supports feature_string, which must be a key
                of the _FEATURE_MAP dictionary.
        
                Will trigger a call to :meth:`.PythonPlugin.module`, which imports the plugin.
                
        """
    def plugin_info_map(self):
        """
        Adds extra adapter-specific information to call to the parent fn.
        """
    def read_from_file(self, filepath, media_linker_name = '__default', media_linker_argument_map = None, hook_function_argument_map = None, **adapter_argument_map):
        """
        Execute the read_from_file function on this adapter.
        
                If read_from_string exists, but not read_from_file, execute that with
                a trivial file object wrapper.
                
        """
    def read_from_string(self, input_str, media_linker_name = '__default', media_linker_argument_map = None, hook_function_argument_map = None, **adapter_argument_map):
        """
        Call the read_from_string function on this adapter.
        """
    def write_to_file(self, input_otio, filepath, hook_function_argument_map = None, **adapter_argument_map):
        """
        Execute the write_to_file function on this adapter.
        
                If write_to_string exists, but not write_to_file, execute that with
                a trivial file object wrapper.
                
        """
    def write_to_string(self, input_otio, hook_function_argument_map = None, **adapter_argument_map):
        """
        Call the write_to_string function on this adapter.
        """
    @property
    def suffixes(self):
        """
        File suffixes associated with this adapter.
        """
    @suffixes.setter
    def suffixes(self, val):
        ...
def _with_linked_media_references(read_otio, media_linker_name, media_linker_argument_map):
    """
    Link media references in the read_otio if possible.
    
        Makes changes in place and returns the read_otio structure back.
        
    """
_FEATURE_MAP: dict = {'read_from_file': ['read_from_file'], 'read_from_string': ['read_from_string'], 'read': ['read_from_file', 'read_from_string'], 'write_to_file': ['write_to_file'], 'write_to_string': ['write_to_string'], 'write': ['write_to_file', 'write_to_string']}
