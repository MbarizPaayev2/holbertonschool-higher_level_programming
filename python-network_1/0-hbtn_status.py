#!/usr/bin/python3
"""This module str """
import urllib.request
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        r = response.read()
        print("Body response:")
        print("type: {}$".format(type(r)))
        print("- content: {}$".format(r))
        print("- utf8 content: {}$".format(r.decode('utf-8')))
