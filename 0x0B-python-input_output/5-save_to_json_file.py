#!/usr/bin/python3
"""
module:  writes an Object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """save a given Object to a text file  with a given name,
    using a JSON representation
    my_pbj: a given object
    filename : str, the name of the output file
    """
    with open(filename, 'w', encoding='utf-8') as FILE:
        json.dump(my_obj, FILE)
