#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    INT_N = 0
    for key in range(len(roman_string)):
        if key > 0 and roman_dict[roman_string[key]] > roman_dict[roman_string[key - 1]]:
            INT_N += roman_dict[roman_string[key]] - \
                2 * roman_dict[roman_string[key - 1]]
        else:
            INT_N += roman_dict[roman_string[key]]
    return INT_N

