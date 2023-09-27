#!/usr/bin/python3
"""Square class"""


class Square:
    """class  constructor function"""

    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")

        self.__size = size

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
