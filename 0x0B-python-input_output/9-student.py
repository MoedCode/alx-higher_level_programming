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

    def to_json(self):
        """Get a Student.dictionary  """
        return self.__dict__  # !/usr/bin/python3
