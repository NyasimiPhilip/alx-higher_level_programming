#!/usr/bin/python3
"""A function that prints a string"""

def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.
    Args:
    first_name (str): The first parameter.
    last_name (str, optional): The second parameter.

    Raises:
    TypeError: If first_name is not a string.
    TypeError: If last_name is not a string.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

