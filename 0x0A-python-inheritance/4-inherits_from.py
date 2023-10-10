#!/usr/bin/python3
""" class/sup class instance checker"""


def inherits_from(obj, a_class):
    """ checks if the given object is an instance of,
             class that inherited (directly or indirectly) from the specified class,
            Return: if it is(True), otherwise (false)
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
