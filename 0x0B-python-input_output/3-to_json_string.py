#!/usr/bin/python3
"""converts python data to json"""
import json


def to_json_string(my_obj):
    """returns json representation of my_obj"""
    json_string = json.dumps(my_obj)
    return json_string
