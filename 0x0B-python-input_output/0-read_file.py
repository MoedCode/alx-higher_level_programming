#!/usr/bin/python3
"function reads from a file"


def read_file(filename=""):
    "function reads from a file"
    with open(filename, "r", encoding="UTF8") as file:
        for line in file:
            print(line, end="")
