#!/usr/bin/python3
"function reads from a file"


def read_file(filename=""):
    "function reads from a file"
    with open(filename, "r", encoding="UTF8") as FILE:
        for line in FILE:
            print(line, end="")
