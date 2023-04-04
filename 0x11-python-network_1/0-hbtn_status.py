#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""

import urllib.request as r

if __name__ == "__main__":
    req = r.Request("https://alx-intranet.hbtn.io/status")
    with r.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
