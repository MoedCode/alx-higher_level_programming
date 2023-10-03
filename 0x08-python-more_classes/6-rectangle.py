#!/usr/bin/python3

"""_summary_"""


class Rectangle:
    """ Rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height*self.__width

    def perimeter(self):

        if (self.height == 0 or self.width == 0):
            return 0

        return (self.__height+self.__width)*2

    def __str__(self):
        str = ""

        if self.width == 0 or self.height == 0:
            return str

        for i in range(self.height):
            str += (self.width*"#")

            if i != self.height-1:
                str += "\n"
        return str

    def __repr__(self):
        return f"Rectangle({self.width:d}, {self.height})"

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
