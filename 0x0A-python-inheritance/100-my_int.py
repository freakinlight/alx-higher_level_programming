#!/usr/bin/python3
"""MyInt: Class that inherits int"""


class MyInt(int):
    """Int operators == and != are inverted"""

    def __eq__(self, value):
        """Override == operator with != operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator."""
        return self.real == value
