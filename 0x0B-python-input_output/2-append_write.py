#!/usr/bin/python3
"""func to append text to file"""


def append_write(filename="", text=""):
    """Appends text to a file.

    Args:
        filename (str): The name of the file.
        text (str): The text to be appended.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written
