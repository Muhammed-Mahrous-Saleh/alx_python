#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""
class NoInitSubclassMeta(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
class BaseGeometry(metaclass=NoInitSubclassMeta):
    """Empty class
    """
    def __dir__(cls):
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
