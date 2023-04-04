#!/usr/bin/python3
"""
takes in a letter and sends the letter
to http://0.0.0.0:5000/search_user as
a parameter
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        var = ""
    else:
        var = sys.argv[1]
    data = {"q": var}
    res = requests.post(url, data=data)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
