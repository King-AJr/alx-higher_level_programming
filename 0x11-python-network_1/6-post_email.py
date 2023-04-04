#!/usr/bin/python3
"""
    take url and email address
    sends request to url with email
    as parameter
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    response = requests.post(url, data=data)
    print(f"{response.text}")
