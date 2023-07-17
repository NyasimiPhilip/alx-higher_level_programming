#!/usr/bin/python3
from models.base import Base
"""class Rectangle that inherits from Base"""


class Rectangle(Base):
    """Class representing a rectangle, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for the Rectangle class.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position (default: 0).
            y (int): The y-coordinate of the rectangle's position (default: 0).
            id (int): The identifier for the rectangle (default: None).
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        
        Args:
            value (int): The width value to be set.
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        
        Args:
            value (int): The height value to be set.
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.
        
        Args:
            value (int): The x-coordinate value to be set.
        
        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position.
        
        Args:
            value (int): The y-coordinate value to be set.
        
        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__height * self.__width

    def display(self):
        """Display the rectangle based on its width and height."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.
        
        Args:
            *args: Variable length arguments.
            **kwargs: Keyword arguments.
        """
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
    @staticmethod
    def load_from_file():
        """Load rectangles from a file and return a list of Rectangle objects."""
        try:
            with open("rectangles.json", "r") as file:
                rectangle_list = []
                rectangles_data = file.read()
                rectangles_dict_list = Base.from_json_string(rectangles_data)
                for rectangle_dict in rectangles_dict_list:
                    rectangle = Rectangle.create(**rectangle_dict)
                    rectangle_list.append(rectangle)
                return rectangle_list
        except FileNotFoundError:
            return []
