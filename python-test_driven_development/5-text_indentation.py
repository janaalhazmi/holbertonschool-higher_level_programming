#!/usr/bin/python3
"""Module containing text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0

    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip(), end="")
