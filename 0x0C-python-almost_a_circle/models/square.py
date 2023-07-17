#!/usr/bin/python3
"""imporing relevant modules"""
from models.rectangle import Rectangle
"""class Square, inherits from Rectangle."""


class Square(Rectangle):
    """A class representing a Square, which inherits from Rectangle."""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
    
    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be greater than 0")
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Update the attributes of the Square.
        
        Args:
            args: Variable-length argument list
            kwargs: Keyword arguments
        """
        if not args:
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']
        else:
            length = len(args)
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.size = args[1]
            if length > 2:
                self.x = args[2]
            if length > 3:
                self.y = args[3]
    
    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        square_dict = super().to_dictionary()
        del square_dict['height']
        del square_dict['width']
        square_dict.update({'size': self.size})
        return square_dict

