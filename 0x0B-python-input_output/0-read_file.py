#!/usr/bin/python3
"""function to read a text file"""


def read_file(filename=""):
    """Reads a text file and prints its content.
    Args:
        filename (str): The name of the file to be read.
        """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
