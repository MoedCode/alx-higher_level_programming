#!/usr/bin/python3
"""fetches X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}

    response = requests.post(url, data=params)
    print(response.text)
