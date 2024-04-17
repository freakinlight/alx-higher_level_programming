#!/usr/bin/python3
"""We define for an object the  lookup function."""


def lookup(obj):
    """Return a list of the object's current attributes."""
    return (dir(obj))
