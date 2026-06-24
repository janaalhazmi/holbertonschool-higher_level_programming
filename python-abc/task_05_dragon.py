#!/usr/bin/python3
"""Module for Dragon and mixins"""


class SwimMixin:
    """Swim mixin"""

    def swim(self):
        """Swim ability"""
        print("The creature swims!")


class FlyMixin:
    """Fly mixin"""

    def fly(self):
        """Fly ability"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""

    def roar(self):
        """Dragon roar"""
        print("The dragon roars!")
