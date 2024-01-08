#!/usr/bin/python3
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":
    URL = sys.argv[1]
    response = requests.get(URL)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
