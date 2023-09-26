#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True
    except (ValueError, TypeError) as e:
        error_message = "Exception: {}".format(e)
        with open(2, "w") as stderr:
            stderr.write(error_message + "\n")
        return False
