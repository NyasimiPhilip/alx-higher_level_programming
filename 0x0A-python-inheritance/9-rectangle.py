#!/usr/bin/python3

"""This script defines the Rectangle class."""
BaseGeometry = import('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Attributes:__width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes a Rectangle object.
        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        Returns:
        int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a readable string representation of the rectangle.
        Returns:
        str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
