#!/usr/bin/python3
""" class/sup class instance checker"""


def is_kind_of_class(obj, a_class):
    """ checks if the given object is an instance of,
        a given class or that inherited from,
        Return: if it is(True), otherwise (false)
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
