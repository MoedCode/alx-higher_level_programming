#!/usr/bin/python3
"""Module for testing the Rectangle class and its related functionality."""
import unittest
import os
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestRectangleMethods(unittest.TestCase):
    """Test suite for the Rectangle class and its methods."""

    def setUp(self):
        """Set up method executed before each test."""
        Base._Base__nb_objects = 0

    def test_area(self):
        """Test the calculation of the area of a Rectangle."""
        new_rectangle = Rectangle(4, 5)
        self.assertEqual(new_rectangle.area(), 20)

    def test_display(self):
        """Test displaying a Rectangle as # characters."""
        new_rectangle = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_rectangle.display()
            self.assertEqual(str_out.getvalue(), "##\n##\n##\n")

    def test_str(self):
        """Test the string representation of a Rectangle."""
        new_rectangle = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(new_rectangle), "[Rectangle] (5) 1/2 - 3/4")

    def test_update(self):
        """Test updating attributes of a Rectangle using positional arguments."""
        new_rectangle = Rectangle(1, 2, 3, 4, 5)
        new_rectangle.update(10, 20, 30)
        self.assertEqual(new_rectangle.id, 10)
        self.assertEqual(new_rectangle.width, 20)
        self.assertEqual(new_rectangle.height, 30)

    def test_update_with_kwargs(self):
        """Test updating attributes of a Rectangle using keyword arguments."""
        new_rectangle = Rectangle(1, 2, 3, 4, 5)
        new_rectangle.update(id=10, height=30)
        self.assertEqual(new_rectangle.id, 10)
        self.assertEqual(new_rectangle.width, 1)
        self.assertEqual(new_rectangle.height, 30)

    def test_to_dictionary(self):
        """Test converting a Rectangle to a dictionary."""
        new_rectangle = Rectangle(5, 6, 7, 8, 9)
        rect_dict = new_rectangle.to_dictionary()
        expected_dict = {'id': 9, 'width': 5, 'height': 6, 'x': 7, 'y': 8}
        self.assertEqual(rect_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
