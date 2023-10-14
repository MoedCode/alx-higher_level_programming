#!/usr/bin/python3
"""Technical preparation."""


def pascal_triangle(n):
    """
returns a list of lists of integers representing the Pascal’s triangle of n:
"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp += [tri[i] + tri[i + 1] ]
        tmp+= [1]
        triangles += [tmp]
    return triangles
"""
121
1
11
121
1331
14641
15101051
"""
if __name__ == "__main__":
    print("pascal's triangle:\n", pascal_triangle(6))