"""
Common utilities used by the file bundle adapters (otiod and otioz).
"""
from __future__ import annotations
import copy as copy
import opentimelineio._otio
from opentimelineio import exceptions
from opentimelineio import schema
from opentimelineio import url_utils
import os as os
import typing
from urllib import parse as urlparse
__all__ = ['BUNDLE_DIR_NAME', 'BUNDLE_PLAYLIST_PATH', 'BUNDLE_VERSION', 'BUNDLE_VERSION_FILE', 'MediaReferencePolicy', 'NotAFileOnDisk', 'copy', 'exceptions', 'os', 'reference_cloned_and_missing', 'schema', 'url_utils', 'urlparse']
class MediaReferencePolicy:
    AllMissing: typing.ClassVar[str] = 'AllMissing'
    ErrorIfNotFile: typing.ClassVar[str] = 'ErrorIfNotFile'
    MissingIfNotFile: typing.ClassVar[str] = 'MissingIfNotFile'
class NotAFileOnDisk(opentimelineio._otio.OTIOError):
    pass
def _guarantee_unique_basenames(path_list, adapter_name):
    ...
def _prepped_otio_for_bundle_and_manifest(input_otio, media_policy, adapter_name):
    """
     Create a new OTIO based on input_otio that has had media references
        replaced according to the media_policy.  Return that new OTIO and a
        mapping of all the absolute file paths (not URLs) to be used in the bundle,
        mapped to MediaReferences associated with those files.  Media references in
        the OTIO will be relinked by the adapters to point to their output
        locations.
    
        The otio[dz] adapters use this function to do further relinking and build
        their bundles.
    
        This is considered an internal API.
        
    """
def _total_file_size_of(filepaths):
    ...
def reference_cloned_and_missing(orig_mr, reason_missing):
    """
    Replace orig_mr with a missing reference with the same metadata.
    
        Also adds original_target_url and missing_reference_because fields.
        
    """
BUNDLE_DIR_NAME: str = 'media'
BUNDLE_PLAYLIST_PATH: str = 'content.otio'
BUNDLE_VERSION: str = '1.0.0'
BUNDLE_VERSION_FILE: str = 'version.txt'
