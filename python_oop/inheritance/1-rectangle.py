#!/usr/bin/env python3
"""Defines a Rectangle class."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
