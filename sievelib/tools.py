# -*- coding: utf-8 -*-

"""Some tools."""

from __future__ import unicode_literals

import six


def to_bytes(s, encoding="utf-8"):
    """Convert a string to bytes."""
    if isinstance(s, six.binary_type):
        return s
    if six.PY3:
        return bytes(s, encoding)
    return s.encode(encoding)
