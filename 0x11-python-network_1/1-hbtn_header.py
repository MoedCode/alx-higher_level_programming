#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.robotparser


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    cmdURL = sys.argv[1]
    reqObj = urllib.request.Request(cmdURL)

    with urllib.request.urlopen(reqObj) as response:
        print(dict(response.headers).get("X-Request-Id"))
