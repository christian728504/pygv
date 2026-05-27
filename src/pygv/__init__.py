"""A minimal, scriptable genome browser for python."""

from ._api import (  # noqa: F401
    Browser,
    Config,
    browse,
    load,
    loads,
    locus,
    ref,
    roi,
    track,
)
from ._version import __version__  # noqa: F401
