#!/usr/bin/python3
"""Importing json module"""
import json
"""class Base"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int): Optional. The ID of the object.

        Returns:
            None
        """
        self.id = id if id is not None else type(self).__nb_objects + 1
        type(self).__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries representing objects.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        instances_list = [obj.to_dictionary() for obj in list_objs]
        list_objs_json = cls.to_json_string(instances_list)
        with open(filename, "w", encoding="utf-8") as myFile:
            myFile.write(list_objs_json)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            list: A list of dictionaries representing objects.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new object using a dictionary of attributes.

        Args:
            **dictionary: Arbitrary keyword arguments representing the attributes of the object.

        Returns:
            object: A new object with the attributes specified in the dictionary.
        """
        Rectangle = __import__('rectangle').Rectangle  # Importing the 'Rectangle' class from the 'rectangle' module
        rect = Rectangle(12, 21, 32, 43, 55)  # Create a 'Rectangle' object with default values
        rect.update(**dictionary)  # Update the 'Rectangle' object with values from the 'dictionary' parameter
        return rect
