#!/usr/bin/python3
""" takes in url, sends request and
    displays request id
"""

import requests
import sys

if __name__ = "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
