#!/usr/bin/python3
"""this is a modul for an append"""


def append_write(filename="", text=""):
    """this is the method"""
    with open(filename, 'a', encoding="utf-8") as file:
         return file.write(text)
