#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Note:
            This attribute is private.
        """
        self.__size = size
