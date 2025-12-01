#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        r = response.read()
        print(r)
