#!/usr/bin/python3
""" IS INSTANCE OF"""


def is_same_class(obj, a_class):
    """Checks if the object instance of the given class
    Returns:
        (True) if object is an instance, (False) if not
    """
    if type(obj) == a_class:
        return True
    else:
        return False
