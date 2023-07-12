#!/usr/bin/python3
"""class that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, other):
        """Override the == operator to invert its behavior"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the != operator to invert its behavior"""
        return not super().__ne__(other)
