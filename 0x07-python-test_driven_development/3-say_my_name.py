#!/usr/bin/python3
"""print names"""


def say_my_name(first_name, last_name=""):
    """recieve names as arguments and print names
    raise exceptions if any of both names is not a string.
    """
    if (type(first_name)) is not str:
        raise TypeError("first_name must be a string")
    if (type(last_name)) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
