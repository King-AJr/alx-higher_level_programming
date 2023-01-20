#!/usr/bin/python3
"""this class is for a rectangle"""

from models.base import Base


class Rectangle(Base):
    """this represents a rectangle instance,with the getter and setter for the properties width, height,x and y axis"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns value for property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value for width and raise error where necessary"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be greater or equal to 0")
        self.__width = value

    @property
    def height(self):
        """return value of property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value for width and raise error where necessary"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """return value for x axis"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value for x axis and raise error where necessary"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be greater than 0")
        self.x = value

    @property
    def y(self):
        """return value for y axis"""
        return self.__y

    @y.setter
    def y(self, value):
        """set value for y axis and raise errornwhere necessary"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("value must be greater than 0")
        self.y = value
