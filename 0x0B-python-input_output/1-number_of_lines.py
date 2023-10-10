#!/usr/bin/python3
"module counts the number of lines of a text file"


def number_of_lines(filename=""):
    "returns the number of lines of a text file"
    with open(filename, "r", encoding="UTF8") as FILE:
        LINE = 0;
        for line in FILE:
            LINE++
    return LINE
