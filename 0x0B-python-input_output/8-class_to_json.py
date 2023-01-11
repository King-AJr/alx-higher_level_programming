#!/usr/bin/python3
"""convert instance of class to json"""
import json


def class_to_json(obj):
    """convert obj to json"""
    return json.dumps(obj.__dict__)
