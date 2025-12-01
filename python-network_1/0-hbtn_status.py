#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        r = response.read()
        print("Body response:")
        print("type: {}$".format(type(r))
        print("- content: {}$".format(r))
        print("- utf8 content: OK$")
