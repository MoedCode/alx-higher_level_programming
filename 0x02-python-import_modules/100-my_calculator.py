#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    argI1 = int(sys.argv[1])
    argI3 = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(argI1, argI3,add(argI1, argI3)))

    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(argI1, argI3,sub(argI1, argI3)))

    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(argI1, argI3,mul(argI1, argI3)))

    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(argI1, argI3,div(argI1, argI3)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
