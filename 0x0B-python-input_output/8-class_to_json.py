#!/usr/bin/python3
"""module : returns dictionary """


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
