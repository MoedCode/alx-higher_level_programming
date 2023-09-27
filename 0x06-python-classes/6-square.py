#!/usr/bin/python3
"""Square class"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position."""
        self.__size = size
        self.position = position

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, raising errors for invalid values."""
        if type(value) != int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square, raising errors for invalid values."""
        if type(value) != tuple:
            raise TypeError('Position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('Position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError('Position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise TypeError('Position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):

        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")

            for _ in range(self.size):
                print("#", end="")
            print("")
