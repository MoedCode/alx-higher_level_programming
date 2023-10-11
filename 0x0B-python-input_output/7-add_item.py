#!/usr/bin/python3
"""
script that adds all arguments to list,
and then save them to a file:
"""
import sys
import os
import os.path
""" os.path module"""
"""  os module"""

Path0 = "add_item.json"

"""  load_from_json_file """
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""  save_to_json_file """
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

if not os.path.exists("path0") or os.stat("path0").st_size == 0:
    save_to_json_file([], "path0")

_argv = load_from_json_file("path0")

for i in range(1, len(sys.argv)):
    _argv += [sys.argv[i]]

save_to_json_file(_argv, "path0")
