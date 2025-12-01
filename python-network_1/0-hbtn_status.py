#!/usr/bin/python3
"""This module fetches status from a URL and prints it."""
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        r = response.read()
        print("Body response:")
        print("type: {}$".format(type(r)))
        print("- content: {}$".format(r))
        print("- utf8 content: {}$".format(r.decode('utf-8')))
