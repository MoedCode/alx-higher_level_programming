#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda element: list(map(lambda i: i*i, element)), matrix))
