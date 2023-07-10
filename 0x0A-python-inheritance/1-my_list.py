#!/usr/bin/python3
"""
A class that inherits from the list class.
"""

class SortedList(list):
"""
A class that inherits from the list class
"""
def print_sorted(self):
    """
    A function that returns the sorted list.
    """
    sorted_list = sorted(self)
    return sorted_list
