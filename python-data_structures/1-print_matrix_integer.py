#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_print = ""
        for number in row:
            if row_print == "":
                row_print = "{}".format(number)
            else:
                row_print = row_print + " {}".format(number)

        print(row_print)