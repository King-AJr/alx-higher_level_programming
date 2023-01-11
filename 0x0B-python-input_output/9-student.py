#!/usr/bin/python3
"""defines a class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dictionary representation of student"""
        return self.__dict__
