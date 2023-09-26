#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error_message = "Exception: {}".format(e)
        with open(2, "w") as stderr:
            stderr.write(error_message + "\n")
        return None
