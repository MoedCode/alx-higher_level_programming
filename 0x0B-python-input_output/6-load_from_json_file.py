#!/usr/bin/python3
"""
module:  writes an Object to a text file
"""

import json


def load_from_json_file(filename):
    """read  given file contain  a json object,
    pares it to object return it
    my_pbj: a given object
    filename : str, the name of the output file
    """
    with open(filename, 'r', encoding='utf-8') as FILE:
        return json.load(FILE)
