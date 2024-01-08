#!/usr/bin/python3
"""
Uses the GitHub API to fetch and display a GitHub user ID based on provided credentials.
Usage: ./10-my_github.py <GitHub_username> <GitHub_password>
  - Utilizes Basic Authentication to access the user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


def display_github_user_id(username, password):
    """
    Fetches and displays a GitHub user ID based on provided credentials.

    Args:
        username (str): GitHub username.
        password (str): GitHub password.

    Returns:
        None
    """
    authentication = HTTPBasicAuth(username, password)
    api_url = "https://api.github.com/user"

    response = requests.get(api_url, auth=authentication)

    if response.status_code == 200:
        user_id = response.json().get("id")
        print("GitHub User ID:", user_id)
    else:
        print("Failed to retrieve GitHub user ID. Check your credentials.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <GitHub_username> <GitHub_password>")
        sys.exit(1)

    github_username = sys.argv[1]
    github_password = sys.argv[2]

    display_github_user_id(github_username, github_password)
