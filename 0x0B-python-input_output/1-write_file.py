#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """writes to a file and creates the file it does not exist"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
