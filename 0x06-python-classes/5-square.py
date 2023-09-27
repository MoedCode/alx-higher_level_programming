#!/usr/bin/python3
"""Square Class - Defines a square and its properties."""


class Square:
    """Square Class - Defines a square and its properties."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
        """
        self.__size = size

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
    def size(self, size):
        """Set the side length of the square.

        Args:
            size (int): The side length to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Print the square using '#' characters.

        If size is 0, an empty line is printed.
        """
        if self.size == 0:
            print("")
            return

        for _ in range(self.size):
            print("#" * self.size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
