#!/usr/bin/env python3
"""This is a class modul for animal"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """this is the main class"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """this is the sub class"""
    def sound(self):
        return 'Bark'

class Cat(Animal):
    """this is another sub class"""
    def sound(self):
        return 'Meow'

