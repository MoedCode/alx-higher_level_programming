#!/usr/bin/python3
"""
Defines a 'Square' class representing squares with equal sides.
This class is a subclass of 'Rectangle' and inherits functionality
related to size validation and area calculation.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square."""

    def __init__(self, size):
        """Initialize a square with a given 'size' for all sides."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
