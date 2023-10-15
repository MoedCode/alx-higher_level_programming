#!/usr/bin/python3
"""Defines a base model class."""
import json


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
    def to_json_string(list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        list_objs (list): A list of inherited Base instances.
        """
        if list_objs is None or len(list_objs) == 0:
            return "[]"
        else:
            return json.dumps([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        rites the JSON string representation of list_objs to a file:
        list_objs: is a list of instances who inherits

        """
        FILE_name = cls.__name__ + ".json"
        with open(FILE_name, "w") as FILE:
            FILE.write(Base.to_json_string(list_objs))
