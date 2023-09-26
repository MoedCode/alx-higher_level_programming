#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    for row in range(len(matrix)):
        for clm in range(len(matrix[row])):
            if clm != len(matrix[row])-1:
                print(matrix[row][clm], end=" ")
            else:
                print("{:d}".format(matrix[row][clm]), end="")
        print("")
