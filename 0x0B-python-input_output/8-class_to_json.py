#!/usr/bin/python3
"""A module for converting a class object to JSON"""

def class_to_json(obj):
    """Converts an instance of a class to a JSON representation.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representing the object's attributes in JSON-like format.
    """
    return obj.__dict__
