#!/usr/bin/python3
""" show git id from github API"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name)

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
