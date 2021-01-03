from __future__ import annotations
import collections as collections
import inspect as inspect
from opentimelineio import core
from opentimelineio import exceptions
from opentimelineio import plugins
import opentimelineio.plugins.python_plugin
from opentimelineio import schemadef
import typing
__all__ = ['SchemaDef', 'available_schemadef_names', 'collections', 'core', 'exceptions', 'from_name', 'inspect', 'module_from_name', 'plugins', 'schemadef']
class SchemaDef(opentimelineio.plugins.python_plugin.PythonPlugin):
    _serializable_label: typing.ClassVar[str] = 'SchemaDef.1'
    def __init__(self, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def module(self):
        """
        
                Return the module object for this schemadef plugin.
                If the module hasn't already been imported, it is imported and
                injected into the otio.schemadefs namespace as a side-effect.
        
                Redefines :py:meth:`.PythonPlugin.module`.
                
        """
    def plugin_info_map(self):
        """
        Adds extra schemadef-specific information to call to the parent fn.
                
        """
def available_schemadef_names():
    """
    Return a string list of the available schemadefs.
    """
def from_name(name):
    """
    Fetch the schemadef plugin object by the name of the schema directly.
    """
def module_from_name(name):
    """
    Fetch the plugin's module by the name of the schemadef.
    
        Will load the plugin if it has not already been loaded.  Reading a file that
        contains the schemadef will also trigger a load of the plugin.
        
    """
