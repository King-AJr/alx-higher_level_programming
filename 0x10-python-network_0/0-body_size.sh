#!/usr/bin/bash
# script takes in a URL, sends a request to that URL, and displays the size of the body of the response

curl -s "$1" | wc -c
