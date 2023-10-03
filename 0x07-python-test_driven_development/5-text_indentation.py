#!/usr/bin/python3
"""summary"""


def text_indentation(text):
    """text_indentation"""
    is_next_whiteSpace = True
    string = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):

        if is_next_whiteSpace and text[i] == " ":
            continue

        is_next_whiteSpace = False

        string += text[i]

        if text[i] == "." or text[i] == "?" or text[i] == ":":

            if i < len(text) - 1 and text[i+1] == " ":
                is_next_whiteSpace = True

            string += "\n\n"

    string = string.rstrip(' ')
    print(string, end="")
