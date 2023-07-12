#!/usr/bin/python3
"""importing json module"""
import json
"""Function to write json to file"""


def save_to_json_file(my_obj, filename):
    """Writes a JSON object to a file.
    
    Args:
        my_obj: The JSON object to be written.
        filename (str): The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
