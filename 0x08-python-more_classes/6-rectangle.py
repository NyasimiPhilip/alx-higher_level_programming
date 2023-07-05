#!/usr/bin/python3

"""
Real Definition of a rectangle
"""


class Rectangle:
    """Class representing a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): The width value to set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to zero.")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int): The height value to set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to zero.")
        self._height = value

    def area(self):
        """Return the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * (self._height + self._width)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self._height == 0 or self._width == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])

    def __repr__(self):
        """Return a string representation of the rectangle object"""
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Destructor for the rectangle object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
