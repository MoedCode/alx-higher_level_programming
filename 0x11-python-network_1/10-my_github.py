#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the GitHub API"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    URL = "https://api.github.com/user"

    response = requests.get(URL, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data["id"])
    else:
        print('None')
