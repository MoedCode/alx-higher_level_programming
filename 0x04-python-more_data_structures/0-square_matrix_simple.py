#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    MAT = []
    for i in range(len(matrix)):
        LIST = []
        for j in range(len(matrix[i])):
            LIST += [matrix[i][j] ** 2]
        MAT += [LIST]
    return (MAT)
