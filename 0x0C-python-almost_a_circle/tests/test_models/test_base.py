#!/usr/bin/python3
"""importing modules"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

"""class to test our classes"""


class TestClasses(unittest.TestCase):
    """class for testing our methods"""

    def setUp(self):
        """setup method"""
        self.rect = Rectangle(5, 10, 2, 4, 123)

    def test_to_json_string(self):
        """test"""
        r1 = Rectangle(8, 6, 3, 9)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_dict = json.loads('[{"x": 3, "width": 8, "id": 1, "height": 6, "y": 9}]')
        actual_dict = json.loads(json_dictionary)
        self.assertEqual(actual_dict, expected_dict)
        new_dict = Base.to_json_string([])
        self.assertEqual(new_dict, "[]")

    def test_from_json_string(self):
        list_input = [
            {'id': 56, 'width': 12, 'height': 5},
            {'id': 2, 'width': 4, 'height': 9}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 5, 'width': 12, 'id': 56}, {'height': 9, 'width': 4, 'id': 2}])
