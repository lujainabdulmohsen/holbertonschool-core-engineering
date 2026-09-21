#!/usr/bin/env python3
"""Defines abstract shapes and shape information."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Represent an abstract shape."""

    @abstractmethod
    def area(self):
        """Return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle."""
        self.radius = radius

    def area(self):
        """Return the circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
