#!/usr/bin/python3
"""The function will add attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object

    Args:
        obj (any): The object to add attribute for.
        att (str): The name of the attribute to be adde in the obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute fails to add.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
