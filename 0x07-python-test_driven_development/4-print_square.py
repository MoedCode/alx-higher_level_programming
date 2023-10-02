#!/usr/bin/python3
"""
Print_square Module:
    Prints square t, using #
"""


def print_square(size):
    """
    print_square
    1. Checks  that `size` is a positive integer.
       if not, raises an error.
    2. Prints square depending on size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    else:
        for row in range(size):
            for col in range(size):
                print('#', end='')
            print()