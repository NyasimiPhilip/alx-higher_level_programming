#!/usr/bin/python3
"""
Function to find the maximum integer in a list
"""

def find_max_integer(integers=[]):
    """
    Function that finds and returns the maximum integer in a list of integers
    If the list is empty, return None
    """
    if len(integers) == 0:
        return None
    max_num = integers[0]
    index = 1
    while index < len(integers):
        if integers[index] > max_num:
            max_num = integers[index]
            index += 1
    return max_num
