#!/usr/bin/python3
"""
module pars string object to  JSON
"""

import json


def from_json_string(my_str):
    """returns object from  JSON string representation"""
    return json.loads(my_str)
