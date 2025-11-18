#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        row = len(matrix)
        for row in matrix:
            print(" ".join("{:d}".format(num) for num in row))

