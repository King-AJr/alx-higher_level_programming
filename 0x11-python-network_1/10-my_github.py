#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

url = 'https://api.github.com/user'
auth = (sys.argv[1], sys.argv[2])

response = requests.get(url, auth=auth)
res = response.json()
print(res.get("id"))
