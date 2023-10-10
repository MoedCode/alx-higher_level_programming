#!/usr/bin/python3
"""
Defines classes for geometric shapes: 'BaseGeometry', 'Rectangle', and 'Square'.
"""


class BaseGeometry:
    """
    A base class with methods for geometric calculations and validation.
    - 'area()' raises an exception.
    - 'integer_validator()' validates that a value is a positive integer.
    """

    def area(self):
        """Raises an exception when called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Represents a rectangle with width and height.
    - 'area()' calculates the area of the rectangle.
    - '__str__()' provides an informal string representation.
    """

    def __init__(self, width, height):
        """Instantiates a rectangle with specified 'width' and 'height'."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Provides an informal string representation of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle with equal sides.
    - 'area()' calculates the area of the square.
    - '__str__()' provides an informal string representation.
    """

    def __init__(self, size):
        """Instantiates a square with a specified 'size' for all sides."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Provides an informal string representation of the square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
