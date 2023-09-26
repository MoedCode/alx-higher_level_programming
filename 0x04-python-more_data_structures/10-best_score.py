#!/usr/bin/python3
def best_score(a_dictionary):
    MAX_INT, KEY_WITH_MAX_INT = -999999999999999, None

    if a_dictionary is None:
        return None

    for KEY in a_dictionary:
        if a_dictionary[KEY] > MAX_INT:
            MAX_INT = a_dictionary[KEY]
            KEY_WITH_MAX_INT = KEY

    return KEY_WITH_MAX_INT
