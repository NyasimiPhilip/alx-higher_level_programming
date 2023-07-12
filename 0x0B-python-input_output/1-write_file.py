#!/usr/bin/python3
"""func to write text to file"""


def write_file(filename="", text=""):
    """
    Writes text to a file.
    Args:
        filename (str): The name of the file.
        text (str): The text to be written.
    Returns:
        int: The number of characters written.
        """
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written
