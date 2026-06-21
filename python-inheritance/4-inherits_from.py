#!/usr/bin/python3
"""this is a modul of inherits_from"""


def inherits_from(obj, a_class):
    """This is the method for the modul"""
    return isinstance(obj, a_class) and type(obj) is not a_class
