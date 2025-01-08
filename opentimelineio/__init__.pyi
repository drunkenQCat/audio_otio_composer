"""
An editorial interchange format and library.

see: http://opentimeline.io

.. moduleauthor:: Contributors to the OpenTimelineIO project <otio-discussion@lists.aswf.io>
"""
from __future__ import annotations
from . import adapters
from . import algorithms
from . import core
from . import exceptions
from . import hooks
from . import media_linker
from . import opentime
from . import plugins
from . import schema
from . import schemadef
from . import url_utils
from . import versioning
__all__ = ['adapters', 'algorithms', 'core', 'exceptions', 'hooks', 'media_linker', 'opentime', 'plugins', 'schema', 'schemadef', 'url_utils', 'versioning']
__author__: str = 'Contributors to the OpenTimelineIO project'
__author_email__: str = 'otio-discussion@lists.aswf.io'
__license__: str = 'Apache 2.0 License'
__version__: str = '0.17.0'
