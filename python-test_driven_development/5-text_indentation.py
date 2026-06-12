#!/usr/bin/python3
"""Module containing text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip = False

    for char in text:
        if skip and char == " ":
            continue

        skip = False

        print(char, end="")

        if char in ".?:":
            print("\n")
            skip = True
