#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            return True
        else:
            return False
    except Exception:
        return False


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if safe_print_integer(my_list[i]):
                print(my_list[i], end="")
                count += 1
        except IndexError:
            continue

    print()
    return count
