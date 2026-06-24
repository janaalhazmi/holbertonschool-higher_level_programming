#!/usr/bin/env python3
"""Shapes module."""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Return area."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
