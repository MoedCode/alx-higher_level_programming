#!/usr/bin/python3

"""fetches X-Request-Id in the response header"""

import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    response = requests.post(URL, data=values)
    print(requests.text)
