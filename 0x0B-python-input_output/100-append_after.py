#!/usr/bin/python3
"""module :  inserts a line of BUFF to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert Search_string  after each line containing new_string in a file.
    Args:
        filename (str): file. name
        search_string (str): string to search for in  the file.
        new_string (str): string to insert.
    """
    BUFF = ""
    with open(filename) as FILE:
        for line in FILE:
            BUFF += line
            if search_string in line:
                BUFF += new_string
    with open(filename, "w") as w:
        w.write(BUFF)
