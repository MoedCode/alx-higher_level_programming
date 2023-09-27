#!/usr/bin/python3

class Square:
    """Define a square with size and position attributes."""

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square, raising errors for invalid values."""
        if type(value) != tuple or len(value) != 2 \
                or not isinstance(value[0], int) or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Print the square using '#' characters."""
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


