#!/usr/bin/python3
"""
takes owner name and repo name
then displays authors for the
last 10 commits
"""

import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    print(url)
    headers = {
            'Authorization': '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'
            }
    params = {'author': sys.argv[2], 'Authorization': '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'}

    response = requests.get(url, headers=headers)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"), commits[i].get("commit").get("author").get("name")))
    except IndexError:
        print("", end="")
