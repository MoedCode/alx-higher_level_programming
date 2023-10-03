#!/usr/bin/python3
"""Documentation for a Rectangle class"""


class Rectangle:
    """A class representing a Rectangle shape"""

    print_symbol = "#"  # Character used for printing the rectangle
    number_of_instances = 0  # Counter for the number of instances created

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle instance.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle instance.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using '#'.
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += [str(self.print_symbol)]
            if i is not self.__height - 1:
                rectangle += ['\n']
        return ''.join(rectangle)

    def __repr__(self):
        """Return a string representation that can be used with eval().

        Returns:
            str: A string representing the constructor of the rectangle.
        """

        eva_str = []
        eva_str += ["Rectangle("]
        eva_str = [str(self.__width) + ", " + str(self.__height) + ')']
        return ''.join(eva_str)

    def __del__(self):
        """Perform actions when an instance is deleted."""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles based on their areas.

        Args:
            rect_1 (Rectangle): The first rectangle for comparison.
            rect_2 (Rectangle): The second rectangle for comparison.

        Returns:
            Rectangle: The larger rectangle or rect_1 in case of equal areas.
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.__width * rect_1.__height
        area2 = rect_2.__width * rect_2.__height

        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2
