#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    New_List = []
    for i in range(list_length):
        try:
            result = 0
            result = my_list_1[i]/my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            continue

        except TypeError:
            print("wrong type")
            continue

        except IndexError:
            print("out of range")
            continue

        finally:
            New_List += [result]

    return New_List
