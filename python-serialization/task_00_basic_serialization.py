#!/usr/bin/env python3
"""this is a function for serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """this is the method"""
    with open(filename, 'w',) as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """this is the method"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
