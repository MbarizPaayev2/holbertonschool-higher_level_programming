#!/usr/bin/python3
"""this is docstr
"""
import requests
import sys
url = sys.argv[1]
#headers = { "X-Request-Id"}
request = requests.get(url)
print(request.headers["X-Request-Id"])
