#!/usr/bin/python3
"""prints content of file"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
