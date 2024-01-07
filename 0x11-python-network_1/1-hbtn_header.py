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
        resObj = dict(response.headers)
        print(f"response object {reqObj}")
        X_request_id = resObj.get("X_Request-Id")
        print(X_request_id)
