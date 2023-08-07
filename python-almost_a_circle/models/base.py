#!/usr/bin/python3
"""Defines a class Base"""

class Base:
    
    __nb_objects = 0

    def __init__(self, id=None):

        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
        