#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the value."""

import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    response = requests.post(URL, data=values)
    print(requests.text)
