#!/usr/bin/python3
"""Function that splits a text according to ., ?, and :"""


def text_indentation(text):
    """This function splits a string of text according to punctuation
    Args:
        text (str): the string of text to split
    Raises:
        TypeError: if the text called with the program is not a string
    """
    for i in range(len(text)):
        if text[i] == ':' or text[i] == '?' or text[i] == '.':
            print(text[i], end="")
            print('$')
            print('$')
        elif text[i] == '\\':
            text[i] ==""
        else:
            print(text[i], end="")
    print('\n')
