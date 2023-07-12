#!/usr/bin/python3
"""importing json module that has the relevant methods"""
import json
"""Function to return json string of object"""


def to_json_string(my_obj):
    """Converts an object to a JSON string representation.
    
    Args:
        my_obj: The object to be converted.
        
    Returns:
        str: The JSON string representation of the object.
    """
    json_string = json.dumps(my_obj)
    return json_string
