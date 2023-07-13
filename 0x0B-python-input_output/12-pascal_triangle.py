#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
              Each sublist represents a row in the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        last_row = triangles[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_element = last_row[i] + last_row[i + 1]
            new_row.append(new_element)
        new_row.append(1)
        triangles.append(new_row)
    return triangles
