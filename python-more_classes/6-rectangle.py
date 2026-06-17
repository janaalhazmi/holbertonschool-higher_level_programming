#!/usr/bin/python3
"""Defines a Rectangle."""


class Rectangle:
    """Rectangle class."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Return rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""

        for i in range(self.__height):
            rectangle += "#" * self.__width

            if i != self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Return a Goodbye message when the rectangle has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
