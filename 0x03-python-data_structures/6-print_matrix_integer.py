#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for row in col:
            if col != [-1]:
                print("{:d}".format(col),end = " ")
            print()
