#!/usr/bin/python3
"""
add_integer - function adds ti umber for unit testing purposes
a : first number
b : second number
Return: sum of a and b
"""


def add_integer(a, b=98):
    """ checks that  a and b atre folat or integer """
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("a and b must be integers or floats")

    # Cast to integer if a is a float
    if isinstance(a, float):
        a = int(a)

    # Cast to integer if b is a float
    if isinstance(b, float):
        b = int(b)

    return a + b
