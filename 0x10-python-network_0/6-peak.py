#!/usr/bin/python3
"""find function"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using a divide and conquer approach.

    Args:
        list_of_integers (list): The list of integers to search for a peak in.

    Returns:
        int or None: The peak integer found in the list, or None if the list is empty.

    Complexity:
        The algorithm has a complexity of O(log(n)).

    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
