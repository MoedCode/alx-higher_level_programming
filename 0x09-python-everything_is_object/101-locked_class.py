#!/usr/bin/python3
"""
This is the documentation for the LockedClass.

LockedClass is a class with a limited set of allowed attributes specified using slots.

Attributes:
first_name: The only allowed attribute for instances of LockedClass.

Methods:
init: Initializes an instance of LockedClass.
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        pass
