#!/usr/bin/python3
""" method that checks if obj is an instance of a_class
"""


def inherits_from(obj, a_class):
    """Function to validate if obj is an instance of a_class
Args:
    obj: The object to check
    a_class: The class to compare against

Returns:
    True if obj is an instance of a_class, False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
