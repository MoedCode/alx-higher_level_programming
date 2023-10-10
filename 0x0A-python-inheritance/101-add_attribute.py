#!/usr/bin/python3

"""Defines a function for adding attributes to objects safely."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if it supports attribute addition.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add.
        value (any): The value for the new attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute to this object.")
    setattr(obj, att, value)
