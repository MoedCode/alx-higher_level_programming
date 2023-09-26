#!/usr/bin/python3
def weight_average(my_list=[]):
    SIZE_OF_LIST = len(my_list)
    T_AVRAGE, W_AVRAGE, MUL = 0, 0, 0

    if SIZE_OF_LIST == 0:
        return 0

    for i in range(SIZE_OF_LIST):
        MUL = 1

        for j in range(len(my_list[i])):
            MUL *= my_list[i][j]

        T_AVRAGE += MUL
        W_AVRAGE += my_list[i][1]

    return T_AVRAGE/W_AVRAGE
