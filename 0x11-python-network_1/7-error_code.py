#!/usr/bin/python3
""",sends a request to the URL and displays the body of the response."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    resObj = requests.get(url)
    if resObj.status_code >= 400:
        print("Error code: {}".format(resObj.status_code))
    else:
        print(resObj.text)
