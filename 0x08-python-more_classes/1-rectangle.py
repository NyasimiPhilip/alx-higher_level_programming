#!/usr/bin/python3
# 1-rectangle.pyclass Rectangle:class Rectangle:
    """Class rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle instance"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value


