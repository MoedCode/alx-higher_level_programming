
#!/usr/bin/python3

"""
       Divide element of a matrix
       Args:
            matrix (list of lists): matrix to be dvided
            div (int or float): the divisor.
        Returns:
                list of lists: A new matrix with elements divided by
                `div`, rounded to 2 decimal places
         Raises:
        TypeError: If `matrix` is not a matrix (list of lists)
        of integers or floats,if each row of the matrix does
        not have the same size,or if `div` is not
        a number (integer or float).
        ZeroDivisionError: If `div` is equal to 0.

       """


def matrix_divided(matrix, div):
    """
    Divide each element of `matrix` by `div` with type checking
    Function is structured as follows:
    1. Check if div in  correct type and value , not zero
    2. Check  if matrix forme, copying  matrix then doing  division
    3. Return the new matrix.
    """
    TEM = "matrix must be a matrix (list of lists) of integers/floats"
    SEM = "Each row of the matrix must have the same size"
    MEM = "div must be a number"
    Result_Matrix = []

    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError(TEM)
    if not isinstance(div, (int, float)):
        raise TypeError(MEM)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_ln = len(matrix[0])
    try:
        for index, row in enumerate(matrix):
            if not isinstance(row, list):
                raise TypeError(TEM)
            if len(row) != row_ln:
                raise TypeError(SEM)
            row_ln = len(row)
            Result_Matrix += [row[:]]
            for rwInd, num in enumerate(row):
                if not isinstance(num, (int, float)):
                    raise TypeError(TEM)
                Result_Matrix[index][rwInd] = round(num/div, 2)

    except:
        raise
    else:
        return Result_Matrix
