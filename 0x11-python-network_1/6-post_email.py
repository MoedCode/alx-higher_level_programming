#!/usr/bin/python3

""" takes in a url, sends a request to the url and displays the value."""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    response = requests.post(url, data=values)
    print(requests.text)
