#!/usr/bin/python3
"""this is a function to insert a new statment after each line"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line after each line containing search_string."""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
