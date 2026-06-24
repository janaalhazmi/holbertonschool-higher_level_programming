#!/usr/bin/python3
"""Module VerboseList class"""
from abc import ABC, abstractmethod


class VerboseList(list):
    """list class with extensions"""

    def append(self, value):
        """Append method"""
        print(f"Added [{value}] to the list.")
        super().append(value)

    def extend(self, value):
        """Extend method"""
        print(f"Extended the list with [{len(value)}] items.")
        super().extend(value)

    def remove(self, value):
        """Remove method"""

        # Checking item
        if value in self:
            print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, value=None):
        """Pop method"""

        # Checking index 
        if value is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            item = super().pop(value)
            print(f"Popped [{item}] from the list.")
            return item

