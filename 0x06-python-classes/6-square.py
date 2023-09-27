#!/usr/bin/python3
"""
Square Class - Defines a square and its properties including size and position.
"""


class Square:
    """
    Square Class - Defines a square and its properties.

    Attributes:
        size (int): The side length of the square.
        position (tuple): The position of the square on the screen.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
            position (tuple, optional): The position of the square (x, y).
                Defaults to (0, 0).
        """
        self.__size = size
        self.position = position

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Get the side length of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the side length of the square.

        Args:
            value (int): The side length to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square on the screen.

        Returns:
            tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square on the screen.

        Args:
            value (tuple): The position to set (x, y).

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Print the square using '#' characters.

        If size is 0, an empty line is printed.
        """
        if self.size == 0:
            print("")
            return

        for _ in range(self.position[1]):
            print("")

        for i in range(self.size):
            for _ in range(self.position[0]):
                if self.position[1] < 0:
                    print(" ", end="")

            for _ in range(self.size):
                print("#", end="")
            print("")
