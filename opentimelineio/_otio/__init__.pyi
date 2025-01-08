"""
Bindings to C++ OTIO implementation
"""
from __future__ import annotations
import opentimelineio._opentime
import typing
__all__ = ['AnyDictionary', 'AnyDictionaryIterator', 'AnyVector', 'AnyVectorIterator', 'Box2d', 'CannotComputeAvailableRangeError', 'Clip', 'Composable', 'Composition', 'CompositionIterator', 'Effect', 'EffectVector', 'EffectVectorIterator', 'ExternalReference', 'FreezeFrame', 'Gap', 'GeneratorReference', 'ImageSequenceReference', 'Item', 'LinearTimeWarp', 'Marker', 'MarkerVector', 'MarkerVectorIterator', 'MediaReference', 'MissingReference', 'NotAChildError', 'OTIOError', 'PyAny', 'SerializableCollection', 'SerializableCollectionIterator', 'SerializableObject', 'SerializableObjectWithMetadata', 'Stack', 'TestObject', 'TimeEffect', 'Timeline', 'Track', 'Transition', 'UnknownSchema', 'UnsupportedSchemaError', 'V2d', 'deserialize_json_from_file', 'deserialize_json_from_string', 'flatten_stack', 'install_external_keepalive_monitor', 'instance_from_schema', 'register_downgrade_function', 'register_serializable_object_type', 'register_upgrade_function', 'release_to_schema_version_map', 'set_type_record', 'type_version_map']
class AnyDictionary:
    def __contains__(self, key):
        ...
    def __copy__(self):
        ...
    def __deepcopy__(self, memo):
        ...
    def __delitem__(self, key: str) -> None:
        ...
    def __eq__(self, other):
        ...
    def __getitem__(self, key: str) -> typing.Any:
        ...
    def __init__(self) -> None:
        ...
    def __internal_setitem__(self, key: str, item: PyAny) -> None:
        ...
    def __iter__(self) -> AnyDictionaryIterator:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self):
        ...
    def __setitem__(self, key, item):
        ...
    def __str__(self):
        ...
    def clear(self):
        """
        D.clear() -> None.  Remove all items from D.
        
        :meta private:
        """
    def get(self, key, default = None):
        """
        D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
        
        :meta private:
        """
    def items(self):
        """
        D.items() -> a set-like object providing a view on D's items
        
        :meta private:
        """
    def keys(self):
        """
        D.keys() -> a set-like object providing a view on D's keys
        
        :meta private:
        """
    def pop(self, key, default = ...):
        ...
    def popitem(self):
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair
                   as a 2-tuple; but raise KeyError if D is empty.
                
        
        :meta private:
        """
    def setdefault(self, key, default_value):
        ...
    def update(self, other = tuple(), **kwds):
        """
         D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
                    If E present and has a .keys() method, does:     for k in E.keys(): D[k] = E[k]
                    If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
                    In either case, this is followed by: for k, v in F.items(): D[k] = v
                
        
        :meta private:
        """
    def values(self):
        """
        D.values() -> an object providing a view on D's values
        
        :meta private:
        """
class AnyDictionaryIterator:
    def __iter__(self) -> AnyDictionaryIterator:
        ...
    def __next__(self) -> typing.Any:
        ...
class AnyVector:
    def __add__(self, other):
        ...
    def __contains__(self, value):
        ...
    def __copy__(self):
        ...
    def __deepcopy__(self, memo = None):
        ...
    def __delitem__(self, index):
        ...
    def __getitem__(self, index):
        ...
    def __iadd__(self, values):
        ...
    def __init__(self) -> None:
        ...
    def __internal_delitem__(self, index: int) -> None:
        ...
    def __internal_getitem__(self, index: int) -> typing.Any:
        ...
    def __internal_insert(self, arg0: int, arg1: PyAny) -> None:
        ...
    def __internal_setitem__(self, index: int, item: PyAny) -> None:
        ...
    def __iter__(self) -> AnyVectorIterator:
        ...
    def __len__(self) -> int:
        ...
    def __radd__(self, other):
        ...
    def __repr__(self):
        ...
    def __reversed__(self):
        ...
    def __setitem__(self, index, item):
        ...
    def __str__(self):
        ...
    def append(self, value):
        """
        S.append(value) -- append value to the end of the sequence
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def clear(self):
        """
        S.clear() -> None -- remove all items from S
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def count(self, value):
        """
        S.count(value) -> integer -- return number of occurrences of value
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def extend(self, values):
        """
        S.extend(iterable) -- extend sequence by appending elements from the iterable
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def index(self, value, start = 0, stop = None):
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
                   Raises ValueError if the value is not present.
        
                   Supporting start and stop arguments is optional, but
                   recommended.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def insert(self, index, item):
        ...
    def pop(self, index = -1):
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def remove(self, value):
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def reverse(self):
        """
        S.reverse() -- reverse *IN PLACE*
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
class AnyVectorIterator:
    def __iter__(self) -> AnyVectorIterator:
        ...
    def __next__(self) -> typing.Any:
        ...
class Box2d:
    __hash__: typing.ClassVar[None] = None
    max: V2d
    min: V2d
    def __eq__(self, arg0: typing.Any) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: V2d) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: V2d, arg1: V2d) -> None:
        ...
    def __ne__(self, arg0: typing.Any) -> bool:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def center(self) -> V2d:
        ...
    @typing.overload
    def extendBy(self, arg0: V2d) -> None:
        ...
    @typing.overload
    def extendBy(self, arg0: Box2d) -> None:
        ...
    @typing.overload
    def intersects(self, arg0: V2d) -> bool:
        ...
    @typing.overload
    def intersects(self, arg0: Box2d) -> bool:
        ...
class CannotComputeAvailableRangeError(OTIOError):
    pass
class Clip(Item):
    """
    
    A :class:`~Clip` is a segment of editable media (usually audio or video).
    
    Contains a :class:`.MediaReference` and a trim on that media reference.
    """
    DEFAULT_MEDIA_KEY: typing.ClassVar[str] = 'DEFAULT_MEDIA'
    active_media_reference_key: str
    media_reference: MediaReference
    def __init__(self, name: str = '', media_reference: MediaReference = None, source_range: opentimelineio._opentime.TimeRange | None = None, metadata: typing.Any = None, active_media_reference: str = 'DEFAULT_MEDIA') -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def find_clips(self, search_range = None):
        ...
    def media_references(self) -> dict[str, MediaReference]:
        ...
    def set_media_references(self, arg0: dict[str, MediaReference], arg1: str) -> None:
        ...
class Composable(SerializableObjectWithMetadata):
    """
    
    An object that can be composed within a :class:`~Composition` (such as :class:`~Track` or :class:`.Stack`).
    """
    def __init__(self, name: str = '', metadata: typing.Any = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def overlapping(self) -> bool:
        ...
    def parent(self) -> Composition:
        ...
    def visible(self) -> bool:
        ...
class Composition(Item):
    """
    
    Base class for an :class:`~Item` that contains :class:`~Composable`\\s.
    
    Should be subclassed (for example by :class:`.Track` and :class:`.Stack`), not used directly.
    """
    def __add__(self, other):
        ...
    def __contains__(self, composable: Composable) -> bool:
        ...
    def __delitem__(self, index):
        ...
    def __getitem__(self, index):
        ...
    def __iadd__(self, values):
        ...
    def __init__(self, name: str = '', children: list[Composable] | None = None, source_range: opentimelineio._opentime.TimeRange | None = None, metadata: typing.Any = None) -> None:
        ...
    def __internal_delitem__(self, index: int) -> None:
        ...
    def __internal_getitem__(self, index: int) -> Composable:
        ...
    def __internal_insert(self, index: int, item: Composable) -> None:
        ...
    def __internal_setitem__(self, index: int, item: Composable) -> None:
        ...
    def __iter__(self) -> CompositionIterator:
        ...
    def __len__(self) -> int:
        ...
    def __radd__(self, other):
        ...
    def __repr__(self):
        ...
    def __reversed__(self):
        ...
    def __setitem__(self, index, item):
        ...
    def __str__(self):
        ...
    def append(self, value):
        """
        S.append(value) -- append value to the end of the sequence
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def child_at_time(self, search_time: opentimelineio._opentime.RationalTime, shallow_search: bool = False) -> Composable:
        ...
    def children_in_range(self, search_range: opentimelineio._opentime.TimeRange) -> list[SerializableObject]:
        ...
    def clear(self):
        """
        S.clear() -> None -- remove all items from S
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def count(self, value):
        """
        S.count(value) -> integer -- return number of occurrences of value
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def extend(self, values):
        """
        S.extend(iterable) -- extend sequence by appending elements from the iterable
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def find_children(self, descended_from_type: typing.Any = None, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
    def handles_of_child(self, child: Composable) -> tuple:
        ...
    def has_clips(self) -> bool:
        ...
    def index(self, value, start = 0, stop = None):
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
                   Raises ValueError if the value is not present.
        
                   Supporting start and stop arguments is optional, but
                   recommended.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def insert(self, index, item):
        ...
    def is_parent_of(self, other: Composable) -> bool:
        ...
    def pop(self, index = -1):
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def range_of_all_children(self) -> dict:
        ...
    def range_of_child(self, child: Composable, reference_space: Composable = None) -> opentimelineio._opentime.TimeRange:
        ...
    def range_of_child_at_index(self, index: int) -> opentimelineio._opentime.TimeRange:
        ...
    def remove(self, value):
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def reverse(self):
        """
        S.reverse() -- reverse *IN PLACE*
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def trim_child_range(self, child_range: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange | None:
        ...
    def trimmed_child_range(self, child_range: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange | None:
        ...
    def trimmed_range_of_child(self, child: Composable, reference_space: Composable = None) -> opentimelineio._opentime.TimeRange | None:
        ...
    def trimmed_range_of_child_at_index(self, index: int) -> opentimelineio._opentime.TimeRange:
        ...
    @property
    def composition_kind(self) -> str:
        ...
class CompositionIterator:
    def __iter__(self) -> CompositionIterator:
        ...
    def __next__(self) -> Composable:
        ...
class Effect(SerializableObjectWithMetadata):
    effect_name: str
    def __init__(self, name: str = '', effect_name: str = '', metadata: typing.Any = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
class EffectVector:
    def __add__(self, other):
        ...
    def __contains__(self, value):
        ...
    def __copy__(self):
        ...
    def __deepcopy__(self, memo = None):
        ...
    def __delitem__(self, index):
        ...
    def __getitem__(self, index):
        ...
    def __iadd__(self, values):
        ...
    def __init__(self) -> None:
        ...
    def __internal_delitem__(self, index: int) -> None:
        ...
    def __internal_getitem__(self, index: int) -> ...:
        ...
    def __internal_insert(self, index: int, item: ...) -> None:
        ...
    def __internal_setitem__(self, index: int, item: ...) -> None:
        ...
    def __iter__(self) -> EffectVectorIterator:
        ...
    def __len__(self) -> int:
        ...
    def __radd__(self, other):
        ...
    def __repr__(self):
        ...
    def __reversed__(self):
        ...
    def __setitem__(self, index, item):
        ...
    def __str__(self):
        ...
    def append(self, value):
        """
        S.append(value) -- append value to the end of the sequence
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def clear(self):
        """
        S.clear() -> None -- remove all items from S
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def count(self, value):
        """
        S.count(value) -> integer -- return number of occurrences of value
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def extend(self, values):
        """
        S.extend(iterable) -- extend sequence by appending elements from the iterable
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def index(self, value, start = 0, stop = None):
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
                   Raises ValueError if the value is not present.
        
                   Supporting start and stop arguments is optional, but
                   recommended.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def insert(self, index, item):
        ...
    def pop(self, index = -1):
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def remove(self, value):
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def reverse(self):
        """
        S.reverse() -- reverse *IN PLACE*
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
class EffectVectorIterator:
    def __iter__(self) -> EffectVectorIterator:
        ...
    def __next__(self) -> ...:
        ...
class ExternalReference(MediaReference):
    target_url: str
    def __init__(self, target_url: str = '', available_range: opentimelineio._opentime.TimeRange | None = None, metadata: typing.Any = None, available_image_bounds: Box2d | None = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
class FreezeFrame(LinearTimeWarp):
    """
    Hold the first frame of the clip for the duration of the clip.
    """
    def __init__(self, name: str = '', metadata: typing.Any = None) -> None:
        ...
class Gap(Item):
    @typing.overload
    def __init__(self, name: str = '', source_range: opentimelineio._opentime.TimeRange = ..., effects: list[Effect] | None = None, markers: list[Marker] | None = None, metadata: typing.Any = None) -> None:
        ...
    @typing.overload
    def __init__(self, name: str = '', duration: opentimelineio._opentime.RationalTime = ..., effects: list[Effect] | None = None, markers: list[Marker] | None = None, metadata: typing.Any = None) -> None:
        ...
class GeneratorReference(MediaReference):
    generator_kind: str
    def __init__(self, name: str = '', generator_kind: str = '', available_range: opentimelineio._opentime.TimeRange | None = None, parameters: typing.Any = None, metadata: typing.Any = None, available_image_bounds: Box2d | None = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    @property
    def parameters(self) -> AnyDictionary:
        ...
class ImageSequenceReference(MediaReference):
    """
    
    An ImageSequenceReference refers to a numbered series of single-frame image files. Each file can be referred to by a URL generated by the :class:`~ImageSequenceReference`.
    
    Image sequences can have URLs with discontinuous frame numbers, for instance if you've only rendered every other frame in a sequence, your frame numbers may be 1, 3, 5, etc. This is configured using the ``frame_step`` attribute. In this case, the 0th image in the sequence is frame 1 and the 1st image in the sequence is frame 3. Because of this there are two numbering concepts in the image sequence, the image number and the frame number.
    
    Frame numbers are the integer numbers used in the frame file name. Image numbers are the 0-index based numbers of the frames available in the reference. Frame numbers can be discontinuous, image numbers will always be zero to the total count of frames minus 1.
    
    An example for 24fps media with a sample provided each frame numbered 1-1000 with a path ``/show/sequence/shot/sample_image_sequence.%04d.exr`` might be
    
    .. code-block:: json
    
        {
          "available_range": {
            "start_time": {
              "value": 0,
              "rate": 24
            },
            "duration": {
              "value": 1000,
              "rate": 24
            }
          },
          "start_frame": 1,
          "frame_step": 1,
          "rate": 24,
          "target_url_base": "file:///show/sequence/shot/",
          "name_prefix": "sample_image_sequence.",
          "name_suffix": ".exr"
          "frame_zero_padding": 4,
        }
    
    The same duration sequence but with only every 2nd frame available in the sequence would be
    
    .. code-block:: json
    
        {
          "available_range": {
            "start_time": {
              "value": 0,
              "rate": 24
            },
            "duration": {
              "value": 1000,
              "rate": 24
            }
          },
          "start_frame": 1,
          "frame_step": 2,
          "rate": 24,
          "target_url_base": "file:///show/sequence/shot/",
          "name_prefix": "sample_image_sequence.",
          "name_suffix": ".exr"
          "frame_zero_padding": 4,
        }
    
    A list of all the frame URLs in the sequence can be generated, regardless of frame step, with the following list comprehension
    
    .. code-block:: python
    
        [ref.target_url_for_image_number(i) for i in range(ref.number_of_images_in_sequence())]
    
    Negative ``start_frame`` is also handled. The above example with a ``start_frame`` of ``-1`` would yield the first three target urls as:
    
    - ``file:///show/sequence/shot/sample_image_sequence.-0001.exr``
    - ``file:///show/sequence/shot/sample_image_sequence.0000.exr``
    - ``file:///show/sequence/shot/sample_image_sequence.0001.exr``
    """
    class MissingFramePolicy:
        """
        Behavior that should be used by applications when an image file in the sequence can't be found on disk.
        
        Members:
        
          error : Application should stop and raise an error.
        
          hold : Application should hold the last available frame before the missing frame.
        
          black : Application should use a black frame in place of the missing frame
        """
        __members__: typing.ClassVar[dict[str, ImageSequenceReference.MissingFramePolicy]]  # value = {'error': <MissingFramePolicy.error: 0>, 'hold': <MissingFramePolicy.hold: 1>, 'black': <MissingFramePolicy.black: 2>}
        black: typing.ClassVar[ImageSequenceReference.MissingFramePolicy]  # value = <MissingFramePolicy.black: 2>
        error: typing.ClassVar[ImageSequenceReference.MissingFramePolicy]  # value = <MissingFramePolicy.error: 0>
        hold: typing.ClassVar[ImageSequenceReference.MissingFramePolicy]  # value = <MissingFramePolicy.hold: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    def __init__(self, target_url_base: str = '', name_prefix: str = '', name_suffix: str = '', start_frame: int = 1, frame_step: int = 1, rate: float = 1, frame_zero_padding: int = 0, missing_frame_policy: ImageSequenceReference.MissingFramePolicy = ..., available_range: opentimelineio._opentime.TimeRange | None = None, metadata: typing.Any = None, available_image_bounds: Box2d | None = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def abstract_target_url(self, symbol):
        """
        
            Generates a target url for a frame where ``symbol`` is used in place
            of the frame number. This is often used to generate wildcard target urls.
            
        """
    def end_frame(self) -> int:
        """
        Last frame number in the sequence based on the :attr:`rate` and :attr:`.available_range`.
        """
    def frame_for_time(self, time: opentimelineio._opentime.RationalTime) -> int:
        """
        Given a :class:`.RationalTime` within the available range, returns the frame number.
        """
    def frame_range_for_time_range(self, time_range):
        """
        Returns first and last frame numbers for
            the given time range in the reference.
        
            :rtype: tuple[int]
            :raises ValueError: if the provided time range is outside the available range.
            
        """
    def number_of_images_in_sequence(self) -> int:
        """
        Returns the number of images based on the :attr:`rate` and :attr:`.available_range`.
        """
    def presentation_time_for_image_number(self, image_number: int) -> opentimelineio._opentime.RationalTime:
        """
        Given an image number, returns the :class:`.RationalTime` at which that image should be shown in the space of :attr:`.available_range`.
        """
    def target_url_for_image_number(self, image_number: int) -> str:
        """
        Given an image number, returns the ``target_url`` for that image.
        
        This is roughly equivalent to:
        
        .. code-block:: python
        
           f"{target_url_prefix}{(start_frame + (image_number * frame_step)):0{value_zero_padding}}{target_url_postfix}"
        """
    @property
    def frame_step(self) -> int:
        """
        Step between frame numbers in file names.
        """
    @frame_step.setter
    def frame_step(self, arg1: int) -> None:
        ...
    @property
    def frame_zero_padding(self) -> int:
        """
        Number of digits to pad zeros out to in frame numbers.
        """
    @frame_zero_padding.setter
    def frame_zero_padding(self, arg1: int) -> None:
        ...
    @property
    def missing_frame_policy(self) -> ImageSequenceReference.MissingFramePolicy:
        """
        Directive for how frames in sequence not found during playback or rendering should be handled.
        """
    @missing_frame_policy.setter
    def missing_frame_policy(self, arg1: ImageSequenceReference.MissingFramePolicy) -> None:
        ...
    @property
    def name_prefix(self) -> str:
        """
        Everything in the file name leading up to the frame number.
        """
    @name_prefix.setter
    def name_prefix(self, arg1: str) -> None:
        ...
    @property
    def name_suffix(self) -> str:
        """
        Everything after the frame number in the file name.
        """
    @name_suffix.setter
    def name_suffix(self, arg1: str) -> None:
        ...
    @property
    def rate(self) -> float:
        """
        Frame rate if every frame in the sequence were played back.
        """
    @rate.setter
    def rate(self, arg1: float) -> None:
        ...
    @property
    def start_frame(self) -> int:
        """
        The first frame number used in file names.
        """
    @start_frame.setter
    def start_frame(self, arg1: int) -> None:
        ...
    @property
    def target_url_base(self) -> str:
        """
        Everything leading up to the file name in the ``target_url``.
        """
    @target_url_base.setter
    def target_url_base(self, arg1: str) -> None:
        ...
class Item(Composable):
    source_range: opentimelineio._opentime.TimeRange | None
    def __init__(self, name: str = '', source_range: opentimelineio._opentime.TimeRange | None = None, effects: list[Effect] | None = None, markers: list[Marker] | None = None, enabled: bool = True, metadata: typing.Any = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def available_range(self) -> opentimelineio._opentime.TimeRange:
        ...
    def duration(self) -> opentimelineio._opentime.RationalTime:
        ...
    def range_in_parent(self) -> opentimelineio._opentime.TimeRange:
        ...
    def transformed_time(self, time: opentimelineio._opentime.RationalTime, to_item: Item) -> opentimelineio._opentime.RationalTime:
        ...
    def transformed_time_range(self, time_range: opentimelineio._opentime.TimeRange, to_item: Item) -> opentimelineio._opentime.TimeRange:
        ...
    def trimmed_range(self) -> opentimelineio._opentime.TimeRange:
        ...
    def trimmed_range_in_parent(self) -> opentimelineio._opentime.TimeRange | None:
        ...
    def visible_range(self) -> opentimelineio._opentime.TimeRange:
        ...
    @property
    def available_image_bounds(self) -> Box2d | None:
        ...
    @property
    def effects(self) -> EffectVector:
        ...
    @property
    def enabled(self) -> bool:
        """
        If true, an Item contributes to compositions. For example, when an audio/video clip is ``enabled=false`` the clip is muted/hidden.
        """
    @enabled.setter
    def enabled(self, arg1: bool) -> None:
        ...
    @property
    def markers(self) -> MarkerVector:
        ...
class LinearTimeWarp(TimeEffect):
    """
    
    A time warp that applies a linear speed up or slow down across the entire clip.
    """
    def __init__(self, name: str = '', time_scalar: float = 1.0, metadata: typing.Any = None) -> None:
        ...
    @property
    def time_scalar(self) -> float:
        """
        Linear time scalar applied to clip. 2.0 means the clip occupies half the time in the parent item, i.e. plays at double speed,
        0.5 means the clip occupies twice the time in the parent item, i.e. plays at half speed.
        
        Note that adjusting the time_scalar of a :class:`~LinearTimeWarp` does not affect the duration of the item this effect is attached to.
        Instead it affects the speed of the media displayed within that item.
        """
    @time_scalar.setter
    def time_scalar(self, arg1: float) -> None:
        ...
class Marker(SerializableObjectWithMetadata):
    """
    
    A marker indicates a marked range of time on an item in a timeline, usually with a name, color or other metadata.
    
    The marked range may have a zero duration. The marked range is in the owning item's time coordinate system.
    """
    class Color:
        BLACK: typing.ClassVar[str] = 'BLACK'
        BLUE: typing.ClassVar[str] = 'BLUE'
        CYAN: typing.ClassVar[str] = 'CYAN'
        GREEN: typing.ClassVar[str] = 'GREEN'
        MAGENTA: typing.ClassVar[str] = 'MAGENTA'
        ORANGE: typing.ClassVar[str] = 'ORANGE'
        PINK: typing.ClassVar[str] = 'PINK'
        PURPLE: typing.ClassVar[str] = 'PURPLE'
        RED: typing.ClassVar[str] = 'RED'
        WHITE: typing.ClassVar[str] = 'WHITE'
        YELLOW: typing.ClassVar[str] = 'YELLOW'
    def __init__(self, name: str = '', marked_range: opentimelineio._opentime.TimeRange = ..., color: str = 'RED', metadata: typing.Any = None, comment: str = '') -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    @property
    def color(self) -> str:
        """
        Color string for this marker (for example: 'RED'), based on the :class:`~Color` enum.
        """
    @color.setter
    def color(self, arg1: str) -> None:
        ...
    @property
    def comment(self) -> str:
        """
        Optional comment for this marker.
        """
    @comment.setter
    def comment(self, arg1: str) -> None:
        ...
    @property
    def marked_range(self) -> opentimelineio._opentime.TimeRange:
        """
        Range this marker applies to, relative to the :class:`.Item` this marker is attached to (e.g. the :class:`.Clip` or :class:`.Track` that owns this marker).
        """
    @marked_range.setter
    def marked_range(self, arg1: opentimelineio._opentime.TimeRange) -> None:
        ...
class MarkerVector:
    def __add__(self, other):
        ...
    def __contains__(self, value):
        ...
    def __copy__(self):
        ...
    def __deepcopy__(self, memo = None):
        ...
    def __delitem__(self, index):
        ...
    def __getitem__(self, index):
        ...
    def __iadd__(self, values):
        ...
    def __init__(self) -> None:
        ...
    def __internal_delitem__(self, index: int) -> None:
        ...
    def __internal_getitem__(self, index: int) -> ...:
        ...
    def __internal_insert(self, index: int, item: ...) -> None:
        ...
    def __internal_setitem__(self, index: int, item: ...) -> None:
        ...
    def __iter__(self) -> MarkerVectorIterator:
        ...
    def __len__(self) -> int:
        ...
    def __radd__(self, other):
        ...
    def __repr__(self):
        ...
    def __reversed__(self):
        ...
    def __setitem__(self, index, item):
        ...
    def __str__(self):
        ...
    def append(self, value):
        """
        S.append(value) -- append value to the end of the sequence
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def clear(self):
        """
        S.clear() -> None -- remove all items from S
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def count(self, value):
        """
        S.count(value) -> integer -- return number of occurrences of value
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def extend(self, values):
        """
        S.extend(iterable) -- extend sequence by appending elements from the iterable
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def index(self, value, start = 0, stop = None):
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
                   Raises ValueError if the value is not present.
        
                   Supporting start and stop arguments is optional, but
                   recommended.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def insert(self, index, item):
        ...
    def pop(self, index = -1):
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def remove(self, value):
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def reverse(self):
        """
        S.reverse() -- reverse *IN PLACE*
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
class MarkerVectorIterator:
    def __iter__(self) -> MarkerVectorIterator:
        ...
    def __next__(self) -> ...:
        ...
class MediaReference(SerializableObjectWithMetadata):
    available_image_bounds: Box2d | None
    available_range: opentimelineio._opentime.TimeRange | None
    def __init__(self, name: str = '', available_range: opentimelineio._opentime.TimeRange | None = None, metadata: typing.Any = None, available_image_bounds: Box2d | None = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    @property
    def is_missing_reference(self) -> bool:
        ...
class MissingReference(MediaReference):
    """
    
    Represents media for which a concrete reference is missing.
    
    Note that a :class:`~MissingReference` may have useful metadata, even if the location of the media is not known.
    """
    def __init__(self, name: str = '', available_range: opentimelineio._opentime.TimeRange | None = None, metadata: typing.Any = None, available_image_bounds: Box2d | None = None) -> None:
        ...
class NotAChildError(OTIOError):
    pass
class OTIOError(Exception):
    pass
class PyAny:
    @typing.overload
    def __init__(self, arg0: bool) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: None) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: SerializableObject) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: opentimelineio._opentime.RationalTime) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: opentimelineio._opentime.TimeRange) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: opentimelineio._opentime.TimeTransform) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: AnyVector) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: AnyDictionary) -> None:
        ...
class SerializableCollection(SerializableObjectWithMetadata):
    """
    
    A container which can hold an ordered list of any serializable objects. Note that this is not a :class:`.Composition` nor is it :class:`.Composable`.
    
    This container approximates the concept of a bin - a collection of :class:`.SerializableObject`\\s that do
    not have any compositional meaning, but can serialize to/from OTIO correctly, with metadata and
    a named collection.
    
    A :class:`~SerializableCollection` is useful for serializing multiple timelines, clips, or media references to a single file.
    """
    def __add__(self, other):
        ...
    def __contains__(self, value):
        ...
    def __delitem__(self, index):
        ...
    def __getitem__(self, index):
        ...
    def __iadd__(self, values):
        ...
    def __init__(self, name: str = '', children: list[SerializableObject] | None = None, metadata: typing.Any = None) -> None:
        ...
    def __internal_delitem__(self, index: int) -> None:
        ...
    def __internal_getitem__(self, index: int) -> SerializableObject:
        ...
    def __internal_insert(self, index: int, item: SerializableObject) -> None:
        ...
    def __internal_setitem__(self, index: int, item: SerializableObject) -> None:
        ...
    def __iter__(self) -> SerializableCollectionIterator:
        ...
    def __len__(self) -> int:
        ...
    def __radd__(self, other):
        ...
    def __repr__(self):
        ...
    def __reversed__(self):
        ...
    def __setitem__(self, index, item):
        ...
    def __str__(self):
        ...
    def append(self, value):
        """
        S.append(value) -- append value to the end of the sequence
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def clear(self):
        """
        S.clear() -> None -- remove all items from S
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def count(self, value):
        """
        S.count(value) -> integer -- return number of occurrences of value
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def extend(self, values):
        """
        S.extend(iterable) -- extend sequence by appending elements from the iterable
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def find_children(self, descended_from_type: typing.Any = None, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
    def index(self, value, start = 0, stop = None):
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
                   Raises ValueError if the value is not present.
        
                   Supporting start and stop arguments is optional, but
                   recommended.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def insert(self, index, item):
        ...
    def pop(self, index = -1):
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def remove(self, value):
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
                
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
    def reverse(self):
        """
        S.reverse() -- reverse *IN PLACE*
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        
        :meta private:
        """
class SerializableCollectionIterator:
    def __iter__(self) -> SerializableCollectionIterator:
        ...
    def __next__(self) -> SerializableObject:
        ...
class SerializableObject:
    """
    Superclass for all classes whose instances can be serialized.
    """
    @staticmethod
    def from_json_file(file_name: str) -> SerializableObject:
        ...
    @staticmethod
    def from_json_string(input: str) -> SerializableObject:
        ...
    def __copy__(self, *args, **kwargs):
        ...
    def __deepcopy__(self, *args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def __setattr__(self, key, value):
        ...
    def clone(self) -> SerializableObject:
        ...
    def deepcopy(self, *args, **kwargs):
        ...
    def is_equivalent_to(self, other: SerializableObject) -> bool:
        ...
    def schema_name(self) -> str:
        ...
    def schema_version(self) -> int:
        ...
    def to_json_file(self, file_name: str, indent: int = 4) -> bool:
        ...
    def to_json_string(self, indent: int = 4) -> str:
        ...
    @property
    def _dynamic_fields(self) -> AnyDictionary:
        ...
    @property
    def is_unknown_schema(self) -> bool:
        ...
class SerializableObjectWithMetadata(SerializableObject):
    def __init__(self, name: str = '', metadata: typing.Any = None) -> None:
        ...
    @property
    def metadata(self) -> AnyDictionary:
        ...
    @property
    def name(self) -> typing.Any:
        ...
    @name.setter
    def name(self, arg1: str) -> None:
        ...
class Stack(Composition):
    def __init__(self, name: str = '', children: list[Composable] | None = None, source_range: opentimelineio._opentime.TimeRange | None = None, markers: list[Marker] | None = None, effects: list[Effect] | None = None, metadata: typing.Any = None) -> None:
        ...
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
class TestObject(SerializableObjectWithMetadata):
    def __init__(self, name: str) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def lookup(self, key: str) -> SerializableObject:
        ...
class TimeEffect(Effect):
    """
    Base class for all effects that alter the timing of an item.
    """
    def __init__(self, name: str = '', effect_name: str = '', metadata: typing.Any = None) -> None:
        ...
class Timeline(SerializableObjectWithMetadata):
    global_start_time: opentimelineio._opentime.RationalTime | None
    tracks: Stack
    def __init__(self, name: str = '', tracks: list[Composable] | None = None, global_start_time: opentimelineio._opentime.RationalTime | None = None, metadata: typing.Any = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def audio_tracks(self) -> list[Track]:
        ...
    def duration(self) -> opentimelineio._opentime.RationalTime:
        ...
    def find_children(self, descended_from_type: typing.Any = None, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
    def range_of_child(self, arg0: Composable) -> opentimelineio._opentime.TimeRange:
        ...
    def video_tracks(self) -> list[Track]:
        ...
class Track(Composition):
    class Kind:
        Audio: typing.ClassVar[str] = 'Audio'
        Video: typing.ClassVar[str] = 'Video'
    class NeighborGapPolicy:
        """
        Members:
        
          around_transitions
        
          never
        """
        __members__: typing.ClassVar[dict[str, Track.NeighborGapPolicy]]  # value = {'around_transitions': <NeighborGapPolicy.around_transitions: 1>, 'never': <NeighborGapPolicy.never: 0>}
        around_transitions: typing.ClassVar[Track.NeighborGapPolicy]  # value = <NeighborGapPolicy.around_transitions: 1>
        never: typing.ClassVar[Track.NeighborGapPolicy]  # value = <NeighborGapPolicy.never: 0>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    kind: str
    def __init__(self, name: str = '', children: list[Composable] | None = None, source_range: opentimelineio._opentime.TimeRange | None = None, kind: str = 'Video', metadata: typing.Any = None) -> None:
        ...
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = None, shallow_search: bool = False) -> list[SerializableObject]:
        ...
    def neighbors_of(self, item: Composable, policy: Track.NeighborGapPolicy = ...) -> tuple:
        ...
class Transition(Composable):
    """
    Represents a transition between the two adjacent items in a :class:`.Track`. For example, a cross dissolve or wipe.
    """
    class Type:
        """
        
        Enum encoding types of transitions.
        
        Other effects are handled by the :class:`Effect` class.
        """
        Custom: typing.ClassVar[str] = 'Custom_Transition'
        SMPTE_Dissolve: typing.ClassVar[str] = 'SMPTE_Dissolve'
    def __init__(self, name: str = '', transition_type: str = '', in_offset: opentimelineio._opentime.RationalTime = ..., out_offset: opentimelineio._opentime.RationalTime = ..., metadata: typing.Any = None) -> None:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def duration(self) -> opentimelineio._opentime.RationalTime:
        ...
    def range_in_parent(self) -> opentimelineio._opentime.TimeRange | None:
        """
        Find and return the range of this item in the parent.
        """
    def trimmed_range_in_parent(self) -> opentimelineio._opentime.TimeRange | None:
        """
        Find and return the timmed range of this item in the parent.
        """
    @property
    def in_offset(self) -> opentimelineio._opentime.RationalTime:
        """
        Amount of the previous clip this transition overlaps, exclusive.
        """
    @in_offset.setter
    def in_offset(self, arg1: opentimelineio._opentime.RationalTime) -> None:
        ...
    @property
    def out_offset(self) -> opentimelineio._opentime.RationalTime:
        """
        Amount of the next clip this transition overlaps, exclusive.
        """
    @out_offset.setter
    def out_offset(self, arg1: opentimelineio._opentime.RationalTime) -> None:
        ...
    @property
    def transition_type(self) -> str:
        """
        Kind of transition, as defined by the :class:`Type` enum.
        """
    @transition_type.setter
    def transition_type(self, arg1: str) -> None:
        ...
class UnknownSchema(SerializableObject):
    @property
    def original_schema_name(self) -> str:
        ...
    @property
    def original_schema_version(self) -> int:
        ...
class UnsupportedSchemaError(OTIOError):
    pass
class V2d:
    __hash__: typing.ClassVar[None] = None
    x: float
    y: float
    @staticmethod
    def baseTypeEpsilon() -> float:
        ...
    @staticmethod
    def baseTypeLowest() -> float:
        ...
    @staticmethod
    def baseTypeMax() -> float:
        ...
    @staticmethod
    def baseTypeSmallest() -> float:
        ...
    @staticmethod
    def dimensions() -> int:
        ...
    def __add__(self, arg0: V2d) -> V2d:
        ...
    def __eq__(self, arg0: typing.Any) -> bool:
        ...
    def __getitem__(self, arg0: int) -> float:
        ...
    def __iadd__(self, arg0: V2d) -> V2d:
        ...
    def __idiv__(self, arg0: V2d) -> V2d:
        ...
    def __imul__(self, arg0: V2d) -> V2d:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None:
        ...
    def __isub__(self, arg0: V2d) -> V2d:
        ...
    def __mod__(self, arg0: typing.Any) -> float:
        ...
    def __mul__(self, arg0: V2d) -> V2d:
        ...
    def __ne__(self, arg0: typing.Any) -> bool:
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def __sub__(self, arg0: V2d) -> V2d:
        ...
    def __truediv__(self, arg0: V2d) -> V2d:
        ...
    def __xor__(self, arg0: typing.Any) -> float:
        ...
    def cross(self, arg0: V2d) -> float:
        ...
    def dot(self, arg0: V2d) -> float:
        ...
    def equalWithAbsError(self, arg0: V2d, arg1: float) -> bool:
        ...
    def equalWithRelError(self, arg0: V2d, arg1: float) -> bool:
        ...
    def length(self) -> float:
        ...
    def length2(self) -> float:
        ...
    def normalize(self) -> V2d:
        ...
    def normalizeExc(self) -> V2d:
        ...
    def normalizeNonNull(self) -> V2d:
        ...
    def normalized(self) -> V2d:
        ...
    def normalizedExc(self) -> V2d:
        ...
    def normalizedNonNull(self) -> V2d:
        ...
def _serialize_json_to_file(value: PyAny, filename: str, schema_version_targets: dict[str, int], indent: int) -> bool:
    ...
def _serialize_json_to_string(value: PyAny, schema_version_targets: dict[str, int], indent: int) -> str:
    ...
def deserialize_json_from_file(filename: str) -> typing.Any:
    """
    Deserialize json file to in-memory objects.
    
    :param str filename: path to json file to read
    
    :returns: root object in the file (usually a Timeline or SerializableCollection)
    :rtype: SerializableObject
    """
def deserialize_json_from_string(input: str) -> typing.Any:
    """
    Deserialize json string to in-memory objects.
    
    :param str input: json string to deserialize
    
    :returns: root object in the string (usually a Timeline or SerializableCollection)
    :rtype: SerializableObject
    """
@typing.overload
def flatten_stack(in_stack: Stack) -> Track:
    ...
@typing.overload
def flatten_stack(tracks: list[Track]) -> Track:
    ...
def install_external_keepalive_monitor(so: SerializableObject, apply_now: bool) -> None:
    ...
def instance_from_schema(schema_name: str, schema_version: int, data: typing.Any) -> SerializableObject:
    """
    Return an instance of the schema from data in the data_dict.
    
    :raises UnsupportedSchemaError: when the requested schema version is greater than the registered schema version.
    """
def register_downgrade_function(schema_name: str, version_to_downgrade_from: int, downgrade_function: typing.Callable[[AnyDictionary], None]) -> bool:
    ...
def register_serializable_object_type(class_object: typing.Any, schema_name: str, schema_version: int) -> None:
    ...
def register_upgrade_function(schema_name: str, version_to_upgrade_to: int, upgrade_function: typing.Callable[[AnyDictionary], None]) -> bool:
    ...
def release_to_schema_version_map() -> dict[str, dict[str, int]]:
    """
    Fetch the compiled in CORE_VERSION_MAP.  
    
    The CORE_VERSION_MAP maps OTIO release versions to maps of schema name to schema version and is autogenerated by the OpenTimelineIO build and release system.  For example: `{"0.15.0": {"Clip": 2, ...}}`
    
    :returns: dictionary mapping core version label to schema_version_map
    :rtype: dict[str, dict[str, int]]
    """
def set_type_record(serializable_obejct: SerializableObject, schema_name: str) -> None:
    ...
def type_version_map() -> dict[str, int]:
    """
    Fetch the currently registered schemas and their versions.
    
    :returns: Map of all registered schema names to their current versions.
    :rtype: dict[str, int]
    """
