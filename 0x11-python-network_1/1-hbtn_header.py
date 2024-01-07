#!/usr/bin/python3

import sys
import urllib.robotparser

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    cmdURL = sys.argv[1]
    print(f"cmd url {sys.argv[1]}")
    reqObj = urllib.request.Request(cmdURL)

    with urllib.request.urlopen(reqObj) as response:
        print(dict(response.headers).get("X-Request-Id"))
