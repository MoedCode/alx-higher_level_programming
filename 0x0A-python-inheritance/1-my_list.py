#!/usr/bin/python3
""" Class """


class MyList(list):
    """ that prints the list, but sorted (ascending sort) """

    def print_sorted(self):
        _list = list()
        _list += self
        _list.sort()
        print(_list)
