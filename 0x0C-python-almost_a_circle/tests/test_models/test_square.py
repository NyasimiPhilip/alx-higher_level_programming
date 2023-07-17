"""importing modules"""
import unittest
import json
from models import square


class TestSquare(unittest.TestCase):
    """class to test square class methods"""
    
    def setUp(self):
        """setup method"""
        self.square = square.Square(7, 10, 32, 8)

    def test_id(self):
        """test method for id"""
        self.assertEqual(self.square.id, 8)  # Check initial id
        self.square.id = 4
        self.assertEqual(self.square.id, 4)  # Check updated id

    def test_area(self):
        """test for area method"""
        self.assertEqual(self.square.area(), 49)  # Check area with initial size
        self.square.size = 5
        self.assertEqual(self.square.area(), 25)  # Check area with updated size

    def test_size(self):
        """method to test size"""
        self.assertEqual(self.square.size, 7)  # Check initial size
        self.square.size = 42
        self.assertEqual(self.square.size, 42)  # Check updated size

        with self.assertRaises(TypeError):
            self.square.size = "32"  # Size cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.square.size = -8  # Size cannot be negative, expect ValueError

    def test_update(self):
        """testing update method"""
        self.square.update(89, 15, 28, 1)
        self.assertEqual(self.square.height, 15)  # Check updated height
        self.assertEqual(self.square.x, 28)  # Check updated x
        self.assertEqual(self.square.id, 89)  # Check updated id

    def test_to_dictionary(self):
        """test method"""
        s1_dict = self.square.to_dictionary()
        self.assertEqual(s1_dict, {'id': 8, 'x': 10, 'size': 7, 'y': 32})  # Check dictionary representation

    def test_str(self):
        """testing __str__ method"""
        self.assertEqual(str(self.square), '[Square] (8) 10/32 - 7')  # Check string representation

