#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv

"""
code ware
leet code
challenging  => code force
"""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Write the JSON serialization of a list of objects to a file.
        list_objs (list): A list of inherited Base instances.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        rites the JSON string representation of list_objs to a file:
        list_objs: is a list of instances who inherits
        """
        FILE_name = cls.__name__ + ".json"
        with open(FILE_name, "w") as FILE:
            if list_objs is None:
                FILE.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                FILE.write(Base.to_json_string(list_dicts))

    # from json to list
    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        json_string:  json string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """Create and return a new object based on its dictionary representation."""

    @classmethod
    def create(cls, **dictionary):
        """Return: class instantiated from a dictionary of attributes.
            **dictionary (dict):  pairs of  Key-value attributes for  initialize instances.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances: from a file
        cls: a class and ,file name must be an <Class name>.json
        example: Rectangle.json
        """
        fileName = str(cls.__name__) + ".json"
        try:
            with open(fileName, "r") as FILE:
                instList = Base.from_json_string(FILE.read())

            return [cls.create(**inst) for inst in instList]

        except:
            IOError("mfesh nasep")
