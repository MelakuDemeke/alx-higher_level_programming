#!/usr/bin/python3
""""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    jsmail = {"email": email}

    r = requests.post(url, data=jsmail)
    print(r.text)
