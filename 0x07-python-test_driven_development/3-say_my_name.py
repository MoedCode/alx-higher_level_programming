
"""
Module:say_my_name
prints a full name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints 2 inputs from type strings with "My name is".
    Raises:
    TypeError: If `first_name` or `last_name` are not strings.
    It accepts one or two arguments.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
