#!/usr/bin/python3
"""Inherited class-checking function, and class definition."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or can be inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
