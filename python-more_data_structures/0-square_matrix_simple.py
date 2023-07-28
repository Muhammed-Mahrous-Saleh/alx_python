#!/usr/bin/python3

def square_matrix_simple(matrix=[[]]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for number in row:
            squared_row.append(number**2)
        squared_matrix.append(squared_row)
    return squared_matrix
