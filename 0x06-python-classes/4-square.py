#!/usr/bin/python3
"""creating a new class"""
class Square:
    """
    new class
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
         """function to retrieve value of size"""
        return self.__size

    @size.setter
    def size(self, value):
         """function to retrieve value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

