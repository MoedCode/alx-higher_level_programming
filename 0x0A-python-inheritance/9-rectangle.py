#!/usr/bin/python3
"""
class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
	""" public e methods area for integer validation"""

	def area(self):
		"""Raises an exception when called."""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""
		Validates that the given 'value' is an integer greater than 0.
		If 'value' is not an integer or is less than or equal to 0, it raises an appropriate error.
		"""
		if type(value) is not int:
			raise TypeError("{:s} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
	"""
	A representation of a rectangle, which is a subclass of BaseGeometry.
	It accepts 'width' and 'height' as parameters during instantiation.
	"""

	def __init__(self, width, height):
		"""Instantiation of the rectangle with 'width' and 'height' attributes."""
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height

	def area(self):
		"""Returns the area of the rectangle."""
		return self.__width * self.__height

	def __str__(self):
		"""Informal string representation of the rectangle."""
		return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
