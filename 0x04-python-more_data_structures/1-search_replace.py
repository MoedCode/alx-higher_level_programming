#!/usr/bin/python3
def search_replace(my_list, search, replace):
    LIST = [[] for _ in range(len(my_list))]
    for  i in range (len(my_list)):
        if (my_list[i] == search):
            LIST[i] = replace
        else:
            LIST[i] = my_list[i]
    return LIST
