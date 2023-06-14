#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use nested map functions to iterate over rows and elements in each row,
    # and compute the square of each element
    squared_matrix = list(map(lambda r: list(map(lambda x: x**2, r)), matrix))
    # Return the squared matrix
    return squared_matrix

