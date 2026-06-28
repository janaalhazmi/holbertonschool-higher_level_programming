#!/usr/bin/python3
"""this is a modul to mae json file"""
import json


def save_to_json_file(my_obj, filename):
    """this is the method"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
