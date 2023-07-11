#!/usr/bin/python3


"""
Function to check if an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):

    """
    Function to check if an object is exactly of a given class
    Args:
    obj: Object to be checked.
    a_class: Class to compare against.
    Returns:
    True if the object is an instance of the given class,
    False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
