#!/usr/bin/python3
"""importing json module"""
import json

"""Funciton too load text from json file"""


def load_from_json_file(filename):
    """Loads JSON data from a file.
    Args:
        filename (str): The name of the file.
    Returns:
        obj: The loaded JSON object.
    """
    with open(filename, encoding="utf-8") as file:
        json_data = file.read()
        return json.loads(json_data)
