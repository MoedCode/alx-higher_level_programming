#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("a and b must be integers or floats")

    # Cast to integer if a is a float
    if isinstance(a, float):
        a = int(a)

    # Cast to integer if b is a float
    if isinstance(b, float):
        b = int(b)

    return a + b

