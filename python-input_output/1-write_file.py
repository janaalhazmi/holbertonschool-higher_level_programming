#!/usr/bin/python3
"""this is a modul for write function"""


def write_file(filename="", text=""):
    """this is the method for the modul"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
