#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argc = len(sys.argv)
if argc < 2:
    print("{} arguments.".format(argc-1))
elif argc == 2:
    print("{} argument:".format(argc-1))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(argc-1))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
