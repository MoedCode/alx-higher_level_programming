#!/usr/bin/python3
"""
class BaseGeometry integer_validator
"""


class BaseGeometry:
    """ public e methods area for integer validation"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """in case of integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
