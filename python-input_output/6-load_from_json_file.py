#!/usr/bin/python3
"""this is a modul for json from file to obj"""
import json


def load_from_json_file(filename):
    """this is the method for json from file to obj"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
