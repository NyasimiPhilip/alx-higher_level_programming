#!/usr/bin/python3
# 10-student.py
"""Defines the Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance with the provided attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is provided and is a list of strings, only the attributes
        specified in the list will be included in the dictionary.

        Args:
            attrs (list): (Optional) A list of attribute names to include.

        Returns:
            dict: A dictionary representation of the Student instance.
                  If attrs is provided, it only includes the specified attributes.
                  Otherwise, it includes all attributes of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
