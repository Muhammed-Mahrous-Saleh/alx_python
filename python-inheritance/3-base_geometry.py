#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry(object):
    """Empty class
    """
    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
