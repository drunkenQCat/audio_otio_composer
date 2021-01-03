"""
Utilities for conversion between urls and file paths
"""
from __future__ import annotations
import os as os
from pathlib import PurePath
from pathlib import PurePosixPath
from pathlib import PureWindowsPath
from urllib import parse as urlparse
from urllib import request
__all__ = ['PurePath', 'PurePosixPath', 'PureWindowsPath', 'filepath_from_url', 'os', 'request', 'url_from_filepath', 'urlparse']
def filepath_from_url(urlstr):
    """
    
        Take an url and return a filepath.
    
        URLs can either be encoded according to the `RFC 3986`_ standard or not.
        Additionally, Windows mapped drive letter and UNC paths need to be accounted for
        when processing URL(s); however, there are `ongoing discussions`_ about how to best
        handle this within Python developer community. This function is meant to cover
        these scenarios in the interim.
    
        .. _RFC 3986: https://tools.ietf.org/html/rfc3986#section-2.1
        .. _ongoing discussions: https://discuss.python.org/t/file-uris-in-python/15600
        
    """
def url_from_filepath(fpath):
    """
    Convert a filesystem path to an url in a portable way using / path sep
    """
