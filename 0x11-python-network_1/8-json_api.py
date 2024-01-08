#!/usr/bin/python3
"""fetches X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    URL = "http://0.0.0.0:5000/search_user"
    params = {"q": q}
    response = requests.post(URL, data=params)
    try:
        json = response.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    except ValueError:
        print("Not a valid JSON")
