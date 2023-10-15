from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance with width, height, x, y, and optional id."""
  # Call the constructor of the parent class (Base)
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
    # print#

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """method that return a special string
        """
        return "[Rectangle] ({}) {}/{} -r {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ in case of positional arguments assigns an argument to each attribute
            in case of keyword arguments assigns Each key in this dictionary
            represents an attribute to the instance
            *args (list): of updatedattribute values.

        """
        argc, kargc = len(args), len(kwargs)

        if args and argc > 0:
            if argc >= 1:
                self.id = args[0]
            if argc >= 2:
                self.width = args[1]
            if argc >= 3:
                self.height = args[2]
            if argc >= 4:
                self.x = args[3]
            if argc >= 4:
                self.y = args[3]
        if kwargs and kargc > 0:
            for key in kwargs:

                if key == 'id':
                    self.id = kwargs[key]

                if key == 'width':
                    self.width = kwargs[key]

                if key == 'height':
                    self.height = kwargs[key]

                if key == 'x':
                    self.x = kwargs[key]

                if key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
