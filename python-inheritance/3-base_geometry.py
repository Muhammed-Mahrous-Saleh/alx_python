#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


def __dir__(self):
    return [attr for attr in dir(type(self)) if attr != '__init_subclass__']


class BaseGeometry(object):
    """Empty class
    """
    pass
