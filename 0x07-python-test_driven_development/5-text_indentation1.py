#!/usr/bin/python3
"""This script defines a function that splits a provided text based on specific punctuation marks."""


def text_indentation(text):
    """This function splits a given text string into segments using certain punctuation marks.

    Args:
        text (str): The input text to be divided.

    Raises:
        TypeError: If the provided input is not a string.
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    text = text.strip()
    while i < len(text):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1
        i += 1
