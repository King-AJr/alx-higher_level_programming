#!/usr/bin/python3
"""converts from json to python object"""
import json


def from_json_string(my_str):
    """returns python object of my_str"""
    obj = json.loads(my_str)
    return obj
