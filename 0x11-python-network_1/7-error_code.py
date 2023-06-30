#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
