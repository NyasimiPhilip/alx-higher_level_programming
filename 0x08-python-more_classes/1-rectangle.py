#!/usr/bin/python3
# 1-rectangle.pyclass Rectangle:
 """Defines a Rectangle class."""
 class Rectangle:
    def __init__(self, width=0, height=0):
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be a non-negative integer")
        self.__width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be a non-negative integer")
        self.__height = value
