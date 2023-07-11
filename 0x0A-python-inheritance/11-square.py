#!/usr/bin/python3
"""class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return super().area()

    def __str__(self):
        """
        Returns a readable string representation of the square.

        Returns:
            str: The string representation of the square.
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
