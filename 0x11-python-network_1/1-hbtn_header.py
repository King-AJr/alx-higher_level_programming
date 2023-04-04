#!/usr/bin/python3
""" takes a url and displays x-request-id """

import urllib.request as r
import sys

if __name__ == "__main__":
    with r.urlopen(sys.argv[1]) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
