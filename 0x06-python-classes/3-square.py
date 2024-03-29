#!/usr/bin/python3
"""creating a new class"""


class Square:
    """
    new class
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        return area of square
        Returns:
        area of square
        """
        return self.__size * self.__size
    
