#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_count = 0  # Initialize a count for printed elements

    try:
        for i in range(x):
            print(my_list[i], end=" ")
            printed_count += 1
    except IndexError:
        pass  # Handle the case where x is greater than the length of my_list

    print()
    return printed_count
