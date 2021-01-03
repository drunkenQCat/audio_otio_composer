"""

HookScripts are plugins that run at defined points ("Hooks").

They expose a ``hook_function`` with signature:

.. py:function:: hook_function(timeline: opentimelineio.schema.Timeline, optional_argument_dict: dict[str, Any]) -> opentimelineio.schema.Timeline  # noqa
   :noindex:

   Hook function signature

Both hook scripts and the hooks they attach to are defined in the plugin
manifest.

Multiple scripts can be attached to a hook. They will be executed in list
order, first to last.

They are defined by the manifests :class:`HookScript`\\s and hooks areas.

.. code-block:: json

   {
       "OTIO_SCHEMA" : "PluginManifest.1",
       "hook_scripts" : [
           {
               "OTIO_SCHEMA" : "HookScript.1",
               "name" : "example hook",
               "filepath" : "example.py"
           }
       ],
       "hooks" : {
           "pre_adapter_write" : ["example hook"],
           "post_adapter_read" : []
       }
   }

The ``hook_scripts`` area loads the python modules with the ``hook_function``\\s to
call in them.  The ``hooks`` area defines the hooks (and any associated
scripts). You can further query and modify these from python.

.. code-block:: python

   import opentimelineio as otio
   hook_list = otio.hooks.scripts_attached_to("some_hook") # -> ['a','b','c']

   # to run the hook scripts:
   otio.hooks.run("some_hook", some_timeline, optional_argument_dict)

This will pass (some_timeline, optional_argument_dict) to ``a``, which will
a new timeline that will get passed into ``b`` with ``optional_argument_dict``,
etc.

To edit the order, change the order in the list:

.. code-block:: python

   hook_list[0], hook_list[2] = hook_list[2], hook_list[0]
   print hook_list # ['c','b','a']

Now ``c`` will run, then ``b``, then ``a``.

To delete a function the list:

.. code-block:: python

   del hook_list[1]

----
"""
from __future__ import annotations
from opentimelineio import core
from opentimelineio import plugins
import opentimelineio.plugins.python_plugin
import typing
__all__ = ['HookScript', 'available_hookscript_names', 'available_hookscripts', 'core', 'names', 'plugins', 'run', 'scripts_attached_to']
class HookScript(opentimelineio.plugins.python_plugin.PythonPlugin):
    _serializable_label: typing.ClassVar[str] = 'HookScript.1'
    def __init__(self, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def run(self, in_timeline, argument_map = {}):
        """
        Run the hook_function associated with this plugin.
        """
def available_hookscript_names():
    """
    Return the names of HookScripts that have been registered.
    """
def available_hookscripts():
    """
    Return the HookScripts objects that have been registered.
    """
def names():
    """
    Return a list of all the registered hooks.
    """
def run(hook, tl, extra_args = None):
    """
    Run all the scripts associated with hook, passing in tl and extra_args.
    
        Will return the return value of the last hook script.
    
        If no hookscripts are defined, returns tl.
        
    """
def scripts_attached_to(hook):
    """
    Return an editable list of all the hook scripts that are attached to
        the specified hook, in execution order.  Changing this list will change the
        order that scripts run in, and deleting a script will remove it from
        executing
        
    """
