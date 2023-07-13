#!/usr/bin/python3
"""Defines a function for inserting text after specific lines in a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a text file.

    Args:
        filename (str): The name of the text file.
        search_string (str): The string to search for within each line of the file.
        new_string (str): The string to insert after each line with the search string.
    """
    modified_text = ""  # The modified text with inserted strings
    with open(filename) as file:
        for line in file:
            modified_text += line  # Append the current line to the modified text
            if search_string in line:
                modified_text += new_string  # Append the new string after the line

    with open(filename, "w") as file:
        file.write(modified_text)  # Overwrite the file with the modified text
