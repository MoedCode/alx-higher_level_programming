#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize a count for printed elements

    try:
        for i in range(x):
            # Try to print the element at index count if it exists
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # If an IndexError occurs (i.e., index out of range), just continue
        pass

    print()  # Print a new line to end the output
    return count
