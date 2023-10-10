#!/usr/bin/python3
""" module: read file """


def read_file(filename=""):
    """ rads file print its content to terminal"""

    with open(filename, "r", encoding="utf-8") as FILE:
        for line in FILE:
            print(line, end=" ")
