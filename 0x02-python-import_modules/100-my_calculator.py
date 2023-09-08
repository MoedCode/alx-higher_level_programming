#!/usr/bin/python3

if __name__ ==  "__main__":
    import sys
    from calculator_1 import add , sub, mul, div
    argc = len(sys.argv)

    if len != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a1 = int(sys.argv[1])
    a3 = int(sys.argv[3])
    if sys.argv == "+":
        print("{} + {} = {}".format(a1, a3, add(a1, a3)))
    if sys.argv == "-":
        print("{} - {} = {}".format(a1, a3, sub(a1, a3)))
    if sys.argv == "*":
        print("{} * {} = {}".format(a1, a3, mul(a1, a3)))
    if sys.argv == "/":
        print("{} / {} = {}".format(a1, a3, div(a1, a3)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
