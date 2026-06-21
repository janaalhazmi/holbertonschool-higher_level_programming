#!/usr/bin/python3
"""Module that defines MyList."""


class MyList(list):
    """Inherited class from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
