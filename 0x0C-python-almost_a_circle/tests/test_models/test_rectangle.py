"""importing modules"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """setup method"""
        self.rect = Rectangle(5, 10, 2, 4, 123)

    def test_init(self):
        """test constructor method"""
        self.assertEqual(self.rect.width, 5)  # Check width
        self.assertEqual(self.rect.id, 123)  # Check id
        self.assertEqual(self.rect.x, 2)  # Check x

    def test_width(self):
        """method to test width method"""
        self.assertEqual(self.rect.width, 5)  # Check initial width
        self.rect.width = 32
        self.assertEqual(self.rect.width, 32)  # Check updated width

        with self.assertRaises(TypeError):
            self.rect.width = "89"  # Width cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.width = -32  # Width cannot be negative, expect ValueError

    def test_height(self):
        """method to test height"""
        self.assertEqual(self.rect.height, 10)  # Check initial height
        self.rect.height = 47
        self.assertEqual(self.rect.height, 47)  # Check updated height

        with self.assertRaises(TypeError):
            self.rect.height = "32"  # Height cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.height = 0  # Height cannot be zero, expect ValueError

    def test_x(self):
        """method to test x"""
        self.assertEqual(self.rect.x, 2)  # Check initial x
        self.rect.x = 30
        self.assertEqual(self.rect.x, 30)  # Check updated x

        with self.assertRaises(TypeError):
            self.rect.x = "39"  # x cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.x = -2  # x cannot be negative, expect ValueError

    def test_y(self):
        """method to test y"""
        self.assertEqual(self.rect.y, 4)  # Check initial y
        self.rect.y = 98
        self.assertEqual(self.rect.y, 98)  # Check updated y

        with self.assertRaises(TypeError):
            self.rect.y = "32"  # y cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.y = -9  # y cannot be negative, expect ValueError

    def test_id(self):
        """testing for id attr"""
        self.assertEqual(self.rect.id, 123)  # Check initial id
        self.rect.id = 4
        self.assertEqual(self.rect.id, 4)  # Check updated id
"""importing modules"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """setup method"""
        self.rect = Rectangle(5, 10, 2, 4, 123)

    def test_init(self):
        """test constructor method"""
        self.assertEqual(self.rect.width, 5)  # Check width
        self.assertEqual(self.rect.id, 123)  # Check id
        self.assertEqual(self.rect.x, 2)  # Check x

    def test_width(self):
        """method to test width method"""
        self.assertEqual(self.rect.width, 5)  # Check initial width
        self.rect.width = 32
        self.assertEqual(self.rect.width, 32)  # Check updated width

        with self.assertRaises(TypeError):
            self.rect.width = "89"  # Width cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.width = -32  # Width cannot be negative, expect ValueError

    def test_height(self):
        """method to test height"""
        self.assertEqual(self.rect.height, 10)  # Check initial height
        self.rect.height = 47
        self.assertEqual(self.rect.height, 47)  # Check updated height

        with self.assertRaises(TypeError):
            self.rect.height = "32"  # Height cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.height = 0  # Height cannot be zero, expect ValueError

    def test_x(self):
        """method to test x"""
        self.assertEqual(self.rect.x, 2)  # Check initial x
        self.rect.x = 30
        self.assertEqual(self.rect.x, 30)  # Check updated x

        with self.assertRaises(TypeError):
            self.rect.x = "39"  # x cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.x = -2  # x cannot be negative, expect ValueError

    def test_y(self):
        """method to test y"""
        self.assertEqual(self.rect.y, 4)  # Check initial y
        self.rect.y = 98
        self.assertEqual(self.rect.y, 98)  # Check updated y

        with self.assertRaises(TypeError):
            self.rect.y = "32"  # y cannot be a string, expect TypeError
        with self.assertRaises(ValueError):
            self.rect.y = -9  # y cannot be negative, expect ValueError

    def test_id(self):
        """testing for id attr"""
        self.assertEqual(self.rect.id, 123)  # Check initial id
        self.rect.id = 4
        self.assertEqual(self.rect.id, 4)  # Check updated id

    def test_area(self):
        """method to test area method"""
        self.assertEqual(self.rect.area(), 50)  # Check area with initial dimensions
        self.rect.width = 3
        self.rect.height = 8
        self.assertEqual(self.rect.area(), 24)  # Check area with updated dimensions

    def test_str(self):
        """test the str() method"""
        self.assertEqual(str(self.rect), '[Rectangle] (123) 2/4 - 5/10')  # Check string representation

    def test_update(self):
        """method to test update method"""
        self.rect.update(height=7, width=12, id=89, y=1)
        self.assertEqual(self.rect.height, 7)  # Check updated height
        self.assertEqual(self.rect.id, 89)  # Check updated id

    def test_to_dictionary(self):
        #convert dict to str first to maintain keys order
        mydictStr = json.dumps(self.rect.to_dictionary())
        self.assertEqual(mydictStr, '{"x": 2, "y": 4, "id": 123, "height": 10, "width": 5}')  # Check dictionary representation

    def test_area(self):
        """method to test area method"""
        self.assertEqual(self.rect.area(), 50)  # Check area with initial dimensions
        self.rect.width = 3
        self.rect.height = 8
        self.assertEqual(self.rect.area(), 24)  # Check area with updated dimensions

    def test_str(self):
        """test the str() method"""
        self.assertEqual(str(self.rect), '[Rectangle] (123) 2/4 - 5/10')  # Check string representation

    def test_update(self):
        """method to test update method"""
        self.rect.update(height=7, width=12, id=89, y=1)
        self.assertEqual(self.rect.height, 7)  # Check updated height
        self.assertEqual(self.rect.id, 89)  # Check updated id

    def test_to_dictionary(self):
        #convert dict to str first to maintain keys order
        mydictStr = json.dumps(self.rect.to_dictionary())
        self.assertEqual(mydictStr, '{"x": 2, "y": 4, "id": 123, "height": 10, "width": 5}')  # Check dictionary representation

