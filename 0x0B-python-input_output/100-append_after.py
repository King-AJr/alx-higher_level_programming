#!/usr/bin/python3
"""define a function that inserts a text into a file"""


def append_after(filename="", search_string="", new_string=""):
    """appends new string to every line containing search string"""
    with open(filename, "r", encoding = "utf-8") as file:
        text = ""
        for line in file:
            text += line;
            if search_string in line:
                with open(filename, "w") as a_file:
                    a_file.write(text)
