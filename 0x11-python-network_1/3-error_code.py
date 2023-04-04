#!/usr/bin/python3
"""takes a url, displays body of response
    also manages urllib and http errors
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            html = response.read()
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        if hasattr(e, "code"):
            print('Error code: ', e.code)
        else:
            print("Error: ",e)
    else:
        print('{}'.format(html.decode("utf-8")))
