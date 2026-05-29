"""cover — Title slide for pitchdecks.

Delegates to the generic cover layout.
"""
from ._base import dispatch

build = dispatch("cover")
