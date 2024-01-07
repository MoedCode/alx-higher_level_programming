#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the value."""

import sys
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    values = {"email": URL}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    reqObj = urllib.request.Request(URL, data)
    with urllib.request.urlopen(reqObj) as response:
        dec_res = response.read.decode('utf-8')
        print(dec_res)
