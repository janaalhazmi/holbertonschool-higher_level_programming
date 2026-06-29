#!/usr/bin/env python3
"""this is a function for CSV"""
import csv
import json


def convert_csv_to_json(filename):
    """this is the method"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = list(csv.DictReader(file))
        with open('data.json', 'w', encoding="utf-8") as file:
            json.dump(data, file)
        return True
    except Exception:
        return False



