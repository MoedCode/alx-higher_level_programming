"""
Module for Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance with width, height, x, y, and an optional id.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int, optional): The x-coordinate of the rectangle's position (default is 0).
        - y (int, optional): The y-coordinate of the rectangle's position (default is 0).
        - id (int, optional): The unique identifier for the rectangle (default is None).

        Returns:
        A new Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get or set the width of the Rectangle.

        - Getter: Retrieve the width of the rectangle.
        - Setter: Set the width of the rectangle.

        Raises:
        - TypeError: If the provided width is not an integer.
        - ValueError: If the provided width is less than or equal to 0.

        Returns:
        The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Get or set the height of the Rectangle.

        - Getter: Retrieve the height of the rectangle.
        - Setter: Set the height of the rectangle.

        Raises:
        - TypeError: If the provided height is not an integer.
        - ValueError: If the provided height is less than or equal to 0.

        Returns:
        The height of the rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Get or set the x-coordinate of the Rectangle.

        - Getter: Retrieve the x-coordinate of the rectangle.
        - Setter: Set the x-coordinate of the rectangle.

        Raises:
        - TypeError: If the provided x-coordinate is not an integer.
        - ValueError: If the provided x-coordinate is less than 0.

        Returns:
        The x-coordinate of the rectangle.
        """
        return self.__x

    @property
    def y(self):
        """
        Get or set the y-coordinate of the Rectangle.

        - Getter: Retrieve the y-coordinate of the rectangle.
        - Setter: Set the y-coordinate of the rectangle.

        Raises:
        - TypeError: If the provided y-coordinate is not an integer.
        - ValueError: If the provided y-coordinate is less than 0.

        Returns:
        The y-coordinate of the rectangle.
        """
        return self.__y

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        Returns:
        The area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle instance to stdout with '#' characters representing its shape.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a special string representation of the Rectangle.

        Returns:
        A formatted string indicating the class name, ID, position, width, and height of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} -r {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
        - *args: Variable length positional arguments representing attribute values.
        - **kwargs: Variable length keyword arguments representing attributes and their values.

        This method allows updating the ID, width, height, x, and y attributes of the Rectangle.

        Example:
        - update(10, 20, x=2, y=3) will update the ID to 10, width to 20, x-coordinate to 2, and y-coordinate to 3.
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
        """
        Return the dictionary representation of a Rectangle instance.

        Returns:
        A dictionary containing the attributes 'id', 'width', 'height', 'x', and 'y'.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
