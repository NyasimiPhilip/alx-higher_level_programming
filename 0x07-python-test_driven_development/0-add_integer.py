#!/usr/bin/python3
# 0-add_integer.py
"""Defines integer addition function."""
def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Arguments are type-checked to be integers or floats.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
