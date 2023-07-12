#!/usr/bin/python3
"""importing module with relevant json methods"""
import json
"""Function to converte json string to object"""


def from_json_string(my_str):
    """Converts a JSON string to an object.
    
    Args:
        my_str (str): The JSON string.
        
    Returns:
        obj: The converted object.
    """
    return json.loads(my_str)
