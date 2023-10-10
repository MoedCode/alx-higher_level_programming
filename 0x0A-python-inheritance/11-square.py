#!/usr/bin/python3
"""
Defines a 'Square' class representing squares with equal sides.
This class inherits from 'Rectangle' and 'BaseGeometry', creating a multi-level inheritance hierarchy.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle, with equal sides.
    - 'area()' calculates the area of the square.
    - '__str__()' provides an informal string representation.
    """

    def __init__(self, size):
        """Initialize a square with a given 'size' for all sides."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Provide an informal string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
