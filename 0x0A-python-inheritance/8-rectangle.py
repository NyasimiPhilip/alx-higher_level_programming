#!/usr/bin/python3
"""Defines the Rectangle class."""

BaseGeometry = import('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Constructor method for Rectangle."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
