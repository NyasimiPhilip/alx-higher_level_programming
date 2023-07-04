#!/usr/bin/python3
# 5-rectangle.py
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = 0
        self._height = 0
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        """Get the width of the Rectangle."""
        return self._width

    def set_width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def get_height(self):
        """Get the height of the Rectangle."""
        return self._height

    def set_height(self, value):
        """Set the height of the Rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ""
        
        rect = []
        for _ in range(self._height):
            rect.append("#" * self._width)
        return "\n".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")

