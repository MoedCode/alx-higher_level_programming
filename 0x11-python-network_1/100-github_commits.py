#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository_name> <repository_owner>
"""

import sys
import requests


def list_recent_commits(repository_name, repository_owner):
    """
    Lists the 10 most recent commits on a given GitHub repository.

    Args:
        repository_name (str): Name of the GitHub repository.
        repository_owner (str): Owner of the GitHub repository.

    Returns:
        None
    """
    api_url = "https://api.github.com/repos/{}/{}/commits".format(
        repository_owner, repository_name)

    response = requests.get(api_url)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <repository_owner>")
        sys.exit(1)

    repository_name = sys.argv[1]
    repository_owner = sys.argv[2]

    list_recent_commits(repository_name, repository_owner)
