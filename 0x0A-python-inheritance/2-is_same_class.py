#!/usr/bin/python3
"""Class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of the given class.

    Args:
        obj (any): The object to get checked.
        a_class (type): The class to match the type of obj.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
