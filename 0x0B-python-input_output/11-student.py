#!/usr/bin/python3
""" class Student that defines a student by"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): student first name.
            last_name (str): student last name  .
            age (int): student age .
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ pars dictionary  of the Student class string representation.
        If attrs is a list of strings just  represents attributes
         then included them in a list.
        Args:
            attrs:  (list) "Optional" , attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
