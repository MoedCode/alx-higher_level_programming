#!/usr/bin/python3
"""
module contains the "Square" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Square inherits from Rectangle
         id, x, y, width and height - this super call will use the logic of
         the __init__ of the Rectangle class. The width and height are
         assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """method that return a special string
        """
        return "[Rectangle] ({}) {}/{} -r {}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ in case of positional arguments assigns an argument to each attribute
            in case of keyword arguments assigns Each key in this dictionary
            represents an attribute to the instance
            *args (list): of updatedattribute values.

        """
        argc, kargc = len(args), len(kwargs)
        if args is None:
            self.__init__(self.size, self.x, self.y)

        if args and argc > 0:
            if argc >= 1:
                self.id = args[0]
            if argc >= 2:
                self.size = args[1]
            if argc >= 3:
                self.x = args[2]
            if argc >= 4:
                self.x = args[3]
            if argc >= 4:
                self.y = args[3]
        if kwargs and kargc > 0:
            for key in kwargs:

                if key == 'id':
                    self.id = kwargs[key]

                if key == 'size':
                    self.size = kwargs[key]

                if key == 'x':
                    self.x = kwargs[key]

                if key == 'y':
                    self.y = kwargs[key]
