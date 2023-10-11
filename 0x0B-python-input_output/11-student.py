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
        dictionary = {}
        if attrs is None:
            return vars(self)
        for i in attrs:
            if i in vars(self).keys():
                dictionary[i] = vars(self)[i]

    def reload_from_json(self, json):

        if json.get("first_name"):
            self.first_name = json["first_name"]

        if json.get("last_name"):
            self.last_name = json["last_name"]

        if json.get("age"):
            self.age = json["age"]
