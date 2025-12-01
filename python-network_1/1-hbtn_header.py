#!/usr/bin/python3
import urllib
import sys
if __name__ == "__main__":
    url = sys.argv[i]
    with urllib.request.urlopen(url) as r:
        read = r.getheader("X-Request-Id")
        print(re)

