"""
Bindings to C++ OTIO implementation
"""

from __future__ import annotations
import typing

__all__ = ["RationalTime", "TimeRange", "TimeTransform"]

class RationalTime:
    """

    The RationalTime class represents a measure of time of :math:`rt.value/rt.rate` seconds.
    It can be rescaled into another :class:`~RationalTime`'s rate.
    """

    @staticmethod
    def duration_from_start_end_time(
        start_time: RationalTime, end_time_exclusive: RationalTime
    ) -> RationalTime:
        """
        Compute the duration of samples from first to last (excluding last). This is not the same as distance.

        For example, the duration of a clip from frame 10 to frame 15 is 5 frames. Result will be in the rate of start_time.
        """

    @staticmethod
    def duration_from_start_end_time_inclusive(
        start_time: RationalTime, end_time_inclusive: RationalTime
    ) -> RationalTime:
        """
        Compute the duration of samples from first to last (including last). This is not the same as distance.

        For example, the duration of a clip from frame 10 to frame 15 is 6 frames. Result will be in the rate of start_time.
        """

    @staticmethod
    def from_frames(frame: float, rate: float) -> RationalTime:
        """
        Turn a frame number and rate into a :class:`~RationalTime` object.
        """

    @staticmethod
    @typing.overload
    def from_seconds(seconds: float, rate: float) -> RationalTime: ...
    @staticmethod
    @typing.overload
    def from_seconds(seconds: float) -> RationalTime: ...
    @staticmethod
    def from_time_string(time_string: str, rate: float) -> RationalTime:
        """
        Convert a time with microseconds string (``HH:MM:ss`` where ``ss`` is an integer or a decimal number) into a :class:`~RationalTime`.
        """

    @staticmethod
    def from_timecode(timecode: str, rate: float) -> RationalTime:
        """
        Convert a timecode string (``HH:MM:SS;FRAME``) into a :class:`~RationalTime`.
        """

    @staticmethod
    def is_valid_timecode_rate(rate: float) -> bool:
        """
        Returns true if the rate is valid for use with timecode.
        """

    @staticmethod
    def nearest_valid_timecode_rate(rate: float) -> float:
        """
        Returns the first valid timecode rate that has the least difference from the given value.
        """

    def __add__(self, arg0: RationalTime) -> RationalTime: ...
    def __copy__(self) -> RationalTime: ...
    def __deepcopy__(self, copier: typing.Any = None) -> RationalTime: ...
    def __eq__(self, arg0: typing.Any) -> bool: ...
    def __ge__(self, arg0: typing.Any) -> bool: ...
    def __gt__(self, arg0: typing.Any) -> bool: ...
    def __iadd__(self, arg0: RationalTime) -> RationalTime: ...
    def __init__(self, value: float = 0, rate: float = 1) -> None: ...
    def __le__(self, arg0: typing.Any) -> bool: ...
    def __lt__(self, arg0: typing.Any) -> bool: ...
    def __ne__(self, arg0: typing.Any) -> bool: ...
    def __neg__(self) -> RationalTime: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __sub__(self, arg0: RationalTime) -> RationalTime: ...
    def almost_equal(self, other: RationalTime, delta: float = 0) -> bool: ...
    def ceil(self) -> RationalTime: ...
    def floor(self) -> RationalTime: ...
    def is_invalid_time(self) -> bool:
        """
        Returns true if the time is invalid. The time is considered invalid if the value or the rate are a NaN value
        or if the rate is less than or equal to zero.
        """

    @typing.overload
    def rescaled_to(self, new_rate: float) -> RationalTime:
        """
        Returns the time value for time converted to new_rate.
        """

    @typing.overload
    def rescaled_to(self, other: RationalTime) -> RationalTime:
        """
        Returns the time for time converted to new_rate.
        """

    def round(self) -> RationalTime: ...
    def strictly_equal(self, other: RationalTime) -> bool: ...
    @typing.overload
    def to_frames(self) -> int:
        """
        Returns the frame number based on the current rate.
        """

    @typing.overload
    def to_frames(self, rate: float) -> int:
        """
        Returns the frame number based on the given rate.
        """

    @typing.overload
    def to_nearest_timecode(self, rate: float, drop_frame: bool | None) -> str:
        """
        Convert to nearest timecode (``HH:MM:SS;FRAME``)
        """

    @typing.overload
    def to_nearest_timecode(self, rate: float) -> str: ...
    @typing.overload
    def to_nearest_timecode(self) -> str: ...
    def to_seconds(self) -> float: ...
    def to_time_string(self) -> str: ...
    @typing.overload
    def to_timecode(self, rate: float, drop_frame: bool | None) -> str:
        """
        Convert to timecode (``HH:MM:SS;FRAME``)
        """

    @typing.overload
    def to_timecode(self, rate: float) -> str: ...
    @typing.overload
    def to_timecode(self) -> str: ...
    @typing.overload
    def value_rescaled_to(self, new_rate: float) -> float:
        """
        Returns the time value for "self" converted to new_rate.
        """

    @typing.overload
    def value_rescaled_to(self, other: RationalTime) -> float: ...
    @property
    def rate(self) -> float: ...
    @property
    def value(self) -> float: ...

class TimeRange:
    """

    The TimeRange class represents a range in time. It encodes the start time and the duration,
    meaning that :meth:`end_time_inclusive` (last portion of a sample in the time range) and
    :meth:`end_time_exclusive` can be computed.
    """

    @staticmethod
    def range_from_start_end_time(
        start_time: RationalTime, end_time_exclusive: RationalTime
    ) -> TimeRange:
        """
        Creates a :class:`~TimeRange` from start and end :class:`~RationalTime`\\s (exclusive).

        For example, if start_time is 1 and end_time is 10, the returned will have a duration of 9.
        """

    @staticmethod
    def range_from_start_end_time_inclusive(
        start_time: RationalTime, end_time_inclusive: RationalTime
    ) -> TimeRange:
        """
        Creates a :class:`~TimeRange` from start and end :class:`~RationalTime`\\s (inclusive).

        For example, if start_time is 1 and end_time is 10, the returned will have a duration of 10.
        """

    def __copy__(self) -> TimeRange: ...
    def __deepcopy__(self, arg0: typing.Any) -> TimeRange: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __init__(
        self, start_time: RationalTime = None, duration: RationalTime = None
    ) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @typing.overload
    def before(
        self, other: RationalTime, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The end of `this` strictly precedes `other` by a value >= `epsilon_s`.
        ::

                     other
                       ↓
           [ this ]    *
        """

    @typing.overload
    def before(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The end of `this` strictly equals the start of `other` and
        the start of `this` strictly equals the end of `other`.
        ::

           [this][other]

        The converse would be ``other.meets(this)``
        """

    @typing.overload
    def begins(
        self, other: RationalTime, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The start of `this` strictly equals `other`.
        ::

           other
             ↓
             *
             [ this ]
        """

    @typing.overload
    def begins(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The start of `this` strictly equals the start of `other`.
        The end of `this` strictly precedes the end of `other` by a value >= `epsilon_s`.
        ::

           [ this ]
           [    other    ]

        The converse would be ``other.begins(this)``
        """

    @typing.overload
    def clamped(self, other: RationalTime) -> RationalTime:
        """
        Clamp 'other' (:class:`~RationalTime`) according to
        :attr:`start_time`/:attr:`end_time_exclusive` and bound arguments.
        """

    @typing.overload
    def clamped(self, other: TimeRange) -> TimeRange:
        """
        Clamp 'other' (:class:`~TimeRange`) according to
        :attr:`start_time`/:attr:`end_time_exclusive` and bound arguments.
        """

    @typing.overload
    def contains(self, other: RationalTime) -> bool:
        """
        The start of `this` precedes `other`.
        `other` precedes the end of `this`.
        ::

                 other
                   ↓
                   *
           [      this      ]
        """

    @typing.overload
    def contains(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The start of `this` precedes start of `other`.
        The end of `this` antecedes end of `other`.
        ::

                [ other ]
           [      this      ]

        The converse would be ``other.contains(this)``
        """

    def duration_extended_by(self, other: RationalTime) -> TimeRange: ...
    def end_time_exclusive(self) -> RationalTime:
        """
        Time of the first sample outside the time range.

        If start frame is 10 and duration is 5, then end_time_exclusive is 15,
        because the last time with data in this range is 14.

        If start frame is 10 and duration is 5.5, then end_time_exclusive is
        15.5, because the last time with data in this range is 15.
        """

    def end_time_inclusive(self) -> RationalTime:
        """
        The time of the last sample containing data in the time range.

        If the time range starts at (0, 24) with duration (10, 24), this will be
        (9, 24)

        If the time range starts at (0, 24) with duration (10.5, 24):
        (10, 24)

        In other words, the last frame with data, even if the last frame is fractional.
        """

    def extended_by(self, other: TimeRange) -> TimeRange:
        """
        Construct a new :class:`~TimeRange` that is this one extended by other.
        """

    @typing.overload
    def finishes(
        self, other: RationalTime, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The end of `this` strictly equals `other`.
        ::

                other
                  ↓
                  *
           [ this ]
        """

    @typing.overload
    def finishes(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The start of `this` strictly antecedes the start of `other` by a value >= `epsilon_s`.
        The end of `this` strictly equals the end of `other`.
        ::

                   [ this ]
           [     other    ]

        The converse would be ``other.finishes(this)``
        """

    def intersects(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The start of `this` precedes or equals the end of `other` by a value >= `epsilon_s`.
        The end of `this` antecedes or equals the start of `other` by a value >= `epsilon_s`.
        ::

           [    this    ]           OR      [    other    ]
                [     other    ]                    [     this    ]

        The converse would be ``other.finishes(this)``
        """

    def meets(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The end of `this` strictly equals the start of `other` and
        the start of `this` strictly equals the end of `other`.
        ::

           [this][other]

        The converse would be ``other.meets(this)``
        """

    @typing.overload
    def overlaps(self, other: RationalTime) -> bool:
        """
        `this` contains `other`.
        ::

                other
                 ↓
                 *
           [    this    ]
        """

    @typing.overload
    def overlaps(
        self, other: TimeRange, epsilon_s: float = 2.6041666666666666e-06
    ) -> bool:
        """
        The start of `this` strictly precedes end of `other` by a value >= `epsilon_s`.
        The end of `this` strictly antecedes start of `other` by a value >= `epsilon_s`.
        ::

           [ this ]
               [ other ]

        The converse would be ``other.overlaps(this)``
        """

    @property
    def duration(self) -> RationalTime: ...
    @property
    def start_time(self) -> RationalTime: ...

class TimeTransform:
    """
    1D transform for :class:`~RationalTime`. Has offset and scale.
    """

    def __copy__(self) -> TimeTransform: ...
    def __deepcopy__(self, memo: dict) -> TimeTransform: ...
    def __eq__(self, arg0: object, /) -> bool: ...
    def __init__(
        self, offset: RationalTime = ..., scale: float = 1, rate: float = -1
    ) -> None: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @typing.overload
    def applied_to(self, other: TimeRange) -> TimeRange: ...
    @typing.overload
    def applied_to(self, other: TimeTransform) -> TimeTransform: ...
    @typing.overload
    def applied_to(self, other: RationalTime) -> RationalTime: ...
    @property
    def offset(self) -> RationalTime: ...
    @property
    def rate(self) -> float: ...
    @property
    def scale(self) -> float: ...
