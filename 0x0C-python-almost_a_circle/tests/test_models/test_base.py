#!/usr/bin/python3
"""Module for testing the Base class and its related functionality."""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestBaseMethods(unittest.TestCase):
    """Test suite for the Base class and its methods."""

    def setUp(self):
        """Set up method executed before each test."""
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test the assignment of an ID to a Base instance."""
        new_instance = Base(1)
        self.assertEqual(new_instance.id, 1)

    def test_default_id(self):
        """Test the default ID assigned to a Base instance."""
        new_instance = Base()
        self.assertEqual(new_instance.id, 1)

    def test_incrementing_id(self):
        """Test that the ID increments for each new Base instance."""
        new_instance1 = Base()
        new_instance2 = Base()
        new_instance3 = Base()
        self.assertEqual(new_instance1.id, 1)
        self.assertEqual(new_instance2.id, 2)
        self.assertEqual(new_instance3.id, 3)

    def test_mix_of_assigned_and_incremented_id(self):
        """Test a mix of assigned and incremented IDs."""
        new_instance1 = Base()
        new_instance2 = Base(1024)
        new_instance3 = Base()
        self.assertEqual(new_instance1.id, 1)
        self.assertEqual(new_instance2.id, 1024)
        self.assertEqual(new_instance3.id, 2)

    def test_string_id(self):
        """Test creating a Base instance with a string as ID."""
        new_instance = Base('1')
        self.assertEqual(new_instance.id, '1')

    def test_more_args_in_init(self):
        """Test passing more arguments to the init method than allowed."""
        with self.assertRaises(TypeError):
            new_instance = Base(1, 1)

    def test_accessing_private_attributes(self):
        """Test attempting to access private attributes of a Base instance."""
        new_instance = Base()
        with self.assertRaises(AttributeError):
            new_instance.__nb_objects

    def test_save_to_file_for_Square(self):
        """Test saving data to a JSON file for Square instances."""
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_for_Rectangle(self):
        """Test saving data to a JSON file for Rectangle instances."""
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
