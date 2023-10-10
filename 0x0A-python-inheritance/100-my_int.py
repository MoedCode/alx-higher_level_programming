#!/usr/bin/python3

"""
Defines a custom class 'MyInt' that inherits from 'int' but reverses the behavior of equality comparisons.
"""


class MyInt(int):
    """
    A custom integer class that behaves in the opposite way for equality comparisons.
    - '==': Compares inequality instead of equality.
    - '!=': Compares equality instead of inequality.
    """
    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Override equality comparison ('==') to compare inequality."""
        return int(self) != other

    def __ne__(self, other):
        """Override inequality comparison ('!=') to compare equality."""
        return int(self) == other
