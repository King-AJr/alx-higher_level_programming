#!/usr/bin/python3
"""appends string to the end of the file"""


def append_write(filename="", text=""):
    """appends string to the end of the file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
