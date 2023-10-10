#!/usr/bin/python3
""" module: read file """


def read_file(filename=""):
    """ rads file print its content to terminal"""
    try:
        with open(filename, "r") as FILE:
            for line in FILE:
                print(line)
    except FileNotFoundError:
        pass
