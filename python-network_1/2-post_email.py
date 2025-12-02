#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
#req = urllib.request.Request(url, method="POST" )
with urllib.request.urlopen(url) as response:
    read = response.read().decode("utf-8")
print("Email: {}".format(email))
 
