#!/usr/bin/python3
import sys
a = sys.argv[1:]
if len(a) == 0:
    print(0)
else:
    res = 0
    for i in a:
        res = res + int(i)
    print(res)
