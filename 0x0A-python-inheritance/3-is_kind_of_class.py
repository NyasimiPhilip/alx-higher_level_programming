#!/usr/bin/python3

"""
Function to check if an object is an instance
of a class or any of its subclasses.
"""


def is_kind_of_class(obj, a_class):

    """
    Function to check if an object is an
    instance of a class or any of its subclasses.
    Args:
    obj: Object to check.
    a_class: Class to compare against.
    Returns:
    True if the object is an instance of the given class or its subclasses,
    False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
