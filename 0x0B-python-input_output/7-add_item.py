#!/usr/bin/python3
"""
script that adds all arguments to list,
and then save them to a file:
"""
import sys
import os.path
import json

Path0 = "add_item.json"
""" function that load_from_json_file """
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

""" function that save_to_json_file """
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
if os.path.exists(Path0):
    with open(Path0, mode="r", encoding="utf-8") as FILE:
        save_to_json_file([], Path0)

""" copy tje file to _argv"""
_argv = load_from_json_file(Path0)

"""  Append arguments to the list"""
for _ in range(1, len(sys.argv)):
    _argv += [sys.argv[_]]

"Save the updated list to the JSON file"
save_to_json_file(_argv, Path0)
