#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if a % b == 0:
            result = a/b
        print("{:d} / {:d} = {}".format(a, b, a/b))
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
