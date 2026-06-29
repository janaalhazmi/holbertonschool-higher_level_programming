#!/usr/bin/env python3
"""this is a class for deserialize and serialize"""
import pickle


class CustomObject:
    """this is the method"""
    def __init__(self, name, age, is_student):
        """this a function for it"""
        self.age = age
        self.name = name
        self.is_student = is_student

    def display(self):
        """a method to display the varibles"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """this is the function for serialize"""
        try:
            with open(filename, 'wb',) as file:
                 pickle.dump(self, file)
        except Exception:
             return None

    @classmethod
    def deserialize(cls, filename):
        """this is for deserialize"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
