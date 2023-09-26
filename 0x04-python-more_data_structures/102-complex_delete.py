#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    DE_KEY_LIST = []

    if a_dictionary is None or value is None:
        return None

    for KEY in a_dictionary:
        if a_dictionary[KEY] == value:
            DE_KEY_LIST.append(KEY)

    if len(DE_KEY_LIST) == 0:
        return a_dictionary

    for i in range(len(DE_KEY_LIST)):
        a_dictionary.pop(DE_KEY_LIST[i])

    return a_dictionary
