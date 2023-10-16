#!/usr/bin/python3
"""
Python package that contains
all necessary attributes.
"""
import json
import csv


class Base:
    """
    The basic class with all basic
    Attributes.
    __nb_objects = 0 : a private attribute to
    manage all instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor function for id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as FILE:
            if list_objs is None:
                FILE.write("[]")
            else:
                inst_list = [o.to_dictionary() for o in list_objs]
                FILE.write(Base.to_json_string(inst_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                inst = cls(1, 1)
            else:
                inst = cls(1)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as FILE:
                inst_list = Base.from_json_string(FILE.read())
                return [cls.create(**inst) for inst in inst_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", instline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    list_attribute = ["id", "width", "height", "x", "y"]
                else:
                    list_attribute = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=list_attribute)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", instline="") as csvfile:
                if cls.__name__ == "Rectangle":
                     list_attribute = ["id", "width", "height", "x", "y"]
                else:
                     list_attribute = ["id", "size", "x", "y"]
                inst_list = csv.DictReader(csvfile, fieldnames= list_attribute)
                inst_list = [dict([k, int(v)] for k, v in d.items())
                              for d in inst_list]
                return [cls.create(**d) for d in inst_list]
        except IOError:
            return []