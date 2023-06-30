#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers.get("X-Request-Id"))
