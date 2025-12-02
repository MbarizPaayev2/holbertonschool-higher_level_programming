#!/usr/bin/python3
"""this is code
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.arg[2]
    response = requests.port(url, data = {'email' : email})
    print("Your email is: {}".format(email)
