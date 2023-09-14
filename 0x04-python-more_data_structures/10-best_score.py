def best_score(a_dictionary):
    KEY_WITH_MAX_INT, MAX_INT = None, -999999999999999

    if a_dictionary == None:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > MAX_INT:
            MAX_INT = a_dictionary[key]
            KEY_WITH_MAX_INT = key
    return KEY_WITH_MAX_INT
