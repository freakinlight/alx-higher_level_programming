#!/usr/bin/python3
"""Iherited list class MyList"""


class MyList(list):
    """Implement sort printing for the list class."""

    def print_sorted(self):
        """Sort ascending order."""
        print(sorted(self))
