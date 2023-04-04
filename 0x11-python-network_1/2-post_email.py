#!/usr/bin/python3
""" take, url and email and sends email to url"""

import urllib.request as r
import urllib.parse as parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    email = parse.urlencode(value)
    email = email.encode('ascii')
    req = r.Request(sys.argv[1], email)
    with r.urlopen(req) as response:
        html = response.read()
        print('{}'.format(html.decode("utf-8")))
