#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    def multiply(num1):
        return num1*number
    new_list = list(map(multiply, my_list))
    return new_list
