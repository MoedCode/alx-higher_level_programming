#!/usr/bin/python3
"""
This script contains a unittest for the max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class defines unittests for the max_integer function.
    """

    def test_max_integer(self):
        """
        Test various cases including edge cases.
        """
        # Test when the list has a single positive element
        self.assertEqual(max_integer([3]), 3)

        # Test when the list has a single negative element
        self.assertEqual(max_integer([-3]), -3)

        # Test when the list is empty
        self.assertEqual(max_integer([]), None)

        # Test when all elements in the list are the same
        self.assertEqual(max_integer([15, 15, 15]), 15)

        # Test when all elements in the list are negative
        self.assertEqual(max_integer([-1, -2, -3]), -1)

        # Test when the maximum element is in the middle
        self.assertEqual(max_integer([15, 10, 5]), 15)

        # Test when there are both positive and negative elements
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)

    def test_type_error(self):
        """
        Test cases where TypeError should be raised.
        """
        # Test when the list contains a string element
        self.assertRaises(TypeError, max_integer, ["h", 1])

        # Test when the list contains a nested list
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])

