#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    LIST = [False] * len(my_list)
    for i in range(len(my_list)):
        LIST[i] = (my_list[i] % 2 == 0)
    return LIST
