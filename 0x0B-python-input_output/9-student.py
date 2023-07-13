#!/usr/bin/python3
"""A class representing a Student"""

class Student:
    """A class representing a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object with the provided attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student object.

        Returns:
            dict: A dictionary containing the attributes of the Student object.
        """
        return self.__dict__
