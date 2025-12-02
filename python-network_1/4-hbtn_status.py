#!/usr/bin/python3
"""this is docstr
"""
import requests
request = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(request)))
print("\t- content: {}".format(request))
