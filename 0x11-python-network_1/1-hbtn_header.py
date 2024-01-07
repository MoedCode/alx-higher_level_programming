#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the value."""

import sys
import urllib.robotparser


if __name__ == "__main__":

    cmdURL = sys.argv[1]
    reqObj = urllib.request.Request(cmdURL)

    with urllib.request.urlopen(reqObj) as response:
        print(dict(response.headers).get("X-Request-Id"))
