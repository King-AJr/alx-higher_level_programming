#!/usr/bin/python3
"""saves python object in a file using json object"""
import json


def save_to_json_file(my_obj, filename):
    """writes my_obj to filename using json strings"""
    string = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(string)
