"""
Exception classes for OpenTimelineIO
"""
from __future__ import annotations
import opentimelineio._otio
from opentimelineio._otio import CannotComputeAvailableRangeError
from opentimelineio._otio import NotAChildError
from opentimelineio._otio import OTIOError
from opentimelineio._otio import UnsupportedSchemaError
__all__: list = ['OTIOError', 'NotAChildError', 'CannotComputeAvailableRangeError', 'UnsupportedSchemaError', 'CouldNotReadFileError', 'NoKnownAdapterForExtensionError', 'ReadingNotSupportedError', 'WritingNotSupportedError', 'NotSupportedError', 'InvalidSerializableLabelError', 'AdapterDoesntSupportFunctionError', 'InstancingNotAllowedError', 'TransitionFollowingATransitionError', 'MisconfiguredPluginError', 'CannotTrimTransitionsError', 'NoDefaultMediaLinkerError']
class AdapterDoesntSupportFunctionError(opentimelineio._otio.OTIOError):
    pass
class CannotTrimTransitionsError(opentimelineio._otio.OTIOError):
    pass
class CouldNotReadFileError(opentimelineio._otio.OTIOError):
    pass
class InstancingNotAllowedError(opentimelineio._otio.OTIOError):
    pass
class InvalidEnvironmentVariableError(opentimelineio._otio.OTIOError):
    pass
class InvalidSerializableLabelError(opentimelineio._otio.OTIOError):
    pass
class MisconfiguredPluginError(opentimelineio._otio.OTIOError):
    pass
class NoDefaultMediaLinkerError(opentimelineio._otio.OTIOError):
    pass
class NoKnownAdapterForExtensionError(opentimelineio._otio.OTIOError):
    pass
class NotSupportedError(opentimelineio._otio.OTIOError):
    pass
class ReadingNotSupportedError(opentimelineio._otio.OTIOError):
    pass
class TransitionFollowingATransitionError(opentimelineio._otio.OTIOError):
    pass
class WritingNotSupportedError(opentimelineio._otio.OTIOError):
    pass
