"""
Core implementation details and wrappers around the C++ library
"""
from __future__ import annotations
from opentimelineio._otio import CannotComputeAvailableRangeError
from opentimelineio._otio import Composable
from opentimelineio._otio import Composition
from opentimelineio._otio import Item
from opentimelineio._otio import MediaReference
from opentimelineio._otio import SerializableObject
from opentimelineio._otio import SerializableObjectWithMetadata
from opentimelineio._otio import Track
from opentimelineio._otio import _serialize_json_to_file
from opentimelineio._otio import _serialize_json_to_string
from opentimelineio._otio import deserialize_json_from_file
from opentimelineio._otio import deserialize_json_from_string
from opentimelineio._otio import flatten_stack
from opentimelineio._otio import install_external_keepalive_monitor
from opentimelineio._otio import instance_from_schema
from opentimelineio._otio import register_downgrade_function
from opentimelineio._otio import register_serializable_object_type
from opentimelineio._otio import register_upgrade_function
from opentimelineio._otio import release_to_schema_version_map
from opentimelineio._otio import set_type_record
from opentimelineio._otio import type_version_map
from opentimelineio.core._core_utils import _add_mutable_mapping_methods
from opentimelineio.core._core_utils import _add_mutable_sequence_methods
from opentimelineio.core._core_utils import _value_to_any
from opentimelineio.core._core_utils import add_method
from . import _core_utils
from . import composable
from . import composition
from . import item
from . import mediaReference
__all__: list = ['Composable', 'Composition', 'Item', 'MediaReference', 'SerializableObject', 'SerializableObjectWithMetadata', 'Track', 'deserialize_json_from_file', 'deserialize_json_from_string', 'flatten_stack', 'install_external_keepalive_monitor', 'instance_from_schema', 'set_type_record', 'add_method', 'upgrade_function_for', 'downgrade_function_from', 'serializable_field', 'deprecated_field', 'serialize_json_to_string', 'serialize_json_to_file', 'register_type', 'type_version_map', 'release_to_schema_version_map']
def deprecated_field():
    """
    For marking attributes on a SerializableObject deprecated.
    """
def downgrade_function_from(cls, version_to_downgrade_from):
    """
    
        Decorator for identifying schema class downgrade functions.
    
        Example:
    
        .. code-block:: python
    
            @downgrade_function_from(MyClass, 5)
            def downgrade_from_five_to_four(data):
                return {"old_attr": data["new_attr"]}
    
        This will get called to downgrade a schema of MyClass from version 5 to
        version 4. MyClass must be a class deriving from
        :class:`~SerializableObject`.
    
        The downgrade function should take a single argument - the dictionary to
        downgrade, and return a dictionary with the fields downgraded.
    
        :param typing.Type[SerializableObject] cls: class to downgrade
        :param int version_to_downgrade_from: the function downgrading from this
                                              version to (version - 1)
        
    """
def register_type(classobj, schemaname = None):
    """
    Decorator for registering a SerializableObject type
    
        Example:
    
        .. code-block:: python
    
            @otio.core.register_type
            class SimpleClass(otio.core.SerializableObject):
              serializable_label = "SimpleClass.2"
              ...
    
        :param typing.Type[SerializableObject] cls: class to register
        :param str schemaname: Schema name (default: parse from serializable_label)
        
    """
def serializable_field(name, required_type = None, doc = None, default_value = None):
    """
    
        Convenience function for adding attributes to child classes of
        :class:`~SerializableObject` in such a way that they will be serialized/deserialized
        automatically.
    
        Use it like this:
    
        .. code-block:: python
    
            @core.register_type
            class Foo(SerializableObject):
                bar = serializable_field("bar", required_type=int, doc="example")
    
        This would indicate that class "foo" has a serializable field "bar".  So:
    
        .. code-block:: python
    
            f = foo()
            f.bar = "stuff"
    
            # serialize & deserialize
            otio_json = otio.adapters.from_name("otio")
            f2 = otio_json.read_from_string(otio_json.write_to_string(f))
    
            # fields should be equal
            f.bar == f2.bar
    
        Additionally, the "doc" field will become the documentation for the
        property.
    
        :param str name: name of the field to add
        :param type required_type: type required for the field
        :param str doc: field documentation
        :param Any default_value: default value to return if no field value is set yet
    
        :return: property object
        :rtype: :py:class:`property`
        
    """
def serialize_json_to_file(root, filename, schema_version_targets = None, indent = 4):
    """
    Serialize root to a json file.  Optionally downgrade resulting schemas
        to schema_version_targets.
    
        :param SerializableObject root: root object to serialize
        :param dict[str, int] schema_version_targets: optional dictionary mapping
                                                      schema name to desired schema
                                                      version, for downgrading the
                                                      result to be compatible with
                                                      older versions of
                                                      OpenTimelineIO.
        :param int indent: number of spaces for each json indentation level. Use -1
                           for no indentation or newlines.
    
        :returns: true for success, false for failure
        :rtype: bool
        
    """
def serialize_json_to_string(root, schema_version_targets = None, indent = 4):
    """
    Serialize root to a json string.  Optionally downgrade resulting schemas
        to schema_version_targets.
    
        :param SerializableObject root: root object to serialize
        :param dict[str, int] schema_version_targets: optional dictionary mapping
                                                      schema name to desired schema
                                                      version, for downgrading the
                                                      result to be compatible with
                                                      older versions of
                                                      OpenTimelineIO.
        :param int indent: number of spaces for each json indentation level. Use -1
                           for no indentation or newlines.
    
        :returns: resulting json string
        :rtype: str
        
    """
def upgrade_function_for(cls, version_to_upgrade_to):
    """
    
        Decorator for identifying schema class upgrade functions.
    
        Example:
    
        .. code-block:: python
    
            @upgrade_function_for(MyClass, 5)
            def upgrade_to_version_five(data):
                pass
    
        This will get called to upgrade a schema of MyClass to version 5. MyClass
        must be a class deriving from :class:`~SerializableObject`.
    
        The upgrade function should take a single argument - the dictionary to
        upgrade, and return a dictionary with the fields upgraded.
    
        Remember that you don't need to provide an upgrade function for upgrades
        that add or remove fields, only for schema versions that change the field
        names.
    
        :param typing.Type[SerializableObject] cls: class to upgrade
        :param int version_to_upgrade_to: the version to upgrade to
        
    """
