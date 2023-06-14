#!/usr/bin/python3
import magic_calculation_102
def magic_calculation(a, b):
    """
    Calculates the magic number between a and b.
    Args:
    a: The first number.
    b: The second number.
    Returns:
    The magic number.
    """
    add = magic_calculation_102.add
    sub = magic_calculation_102.sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c += i
            return c
    else:
        return sub(a, b)
