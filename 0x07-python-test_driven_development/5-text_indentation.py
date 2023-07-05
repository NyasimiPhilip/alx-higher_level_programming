#!/usr/bin/python3

5-text_indentation.py
"""Defines a function for text indentation."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == " ":
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n\n")
            c += 1
            while c < len(text) and text[c] == " ":
                c += 1
            continue
        c += 1

