#!/usr/bin/python3
"""Module that takes in a URL and an email, sends a POST request to the url"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    jsonemil = {"email": email}
    data = urllib.parse.urlencode(jsonemil).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
