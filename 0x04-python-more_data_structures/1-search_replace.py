#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_list = [[] for _ in range(len(my_list))]
    for i in range(len(my_list)):
        if my_list[i] == search:
            result_list[i] = replace
        else:
            result_list[i] = my_list[i]
    return result_list
