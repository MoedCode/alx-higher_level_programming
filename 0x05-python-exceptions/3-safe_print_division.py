#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a/b
        print("{:d} / {:d} = {:.1f}".format(a, b, result))
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
