#!/usr/bin/python3
"""
module counts the number of lines of a text file
"""


def write_file(filename="", text=""):
    """
    write_file: write given buffer to file
    if file does not exist it creates one
    with a given file name
    text: buffer to be written to file
    filename: target file where buffer is to be written
    returns:the number of lines of a text file
    """
    with open(filename, "w+") as file:
        return file.write(text)
