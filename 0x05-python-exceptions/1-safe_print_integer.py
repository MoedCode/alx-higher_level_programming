#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, int):
        print("{:d}".format(value))
        return True
    else:
        print("{} is not an integer".format(value))
        return False
