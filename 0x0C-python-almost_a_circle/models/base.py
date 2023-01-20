#!/usr/bin/python3
"""This module defines a base class"""


class Base:
    """this class assigns an id to an unassigned instance"""

    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) is int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
