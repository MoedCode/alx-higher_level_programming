#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class constructor function """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ __position property getter method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """value property getter method"""
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):

        if self.size == 0:
            print()
            return

        for k in range(self.position[1]):
            print("")

        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")

            for j in range(self.size):
                print("#", end="")
            print("")
