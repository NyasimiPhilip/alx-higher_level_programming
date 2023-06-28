#!/usr/bin/python3
"""creating a new class"""

class Square:
  """
    new Square class
    """
    def __init__(self, size):
       """Initialize a new square."""
        self.__size = size

    @property
    def size(self):
      """
      function to retrieve value of size
      """
        return self.__size

    @size.setter
    def size(self, value):
        """function to set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
      """Return the area."""
      return self.__size ** 2

    def my_print(self):
      """function that prints square with # symbols"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
