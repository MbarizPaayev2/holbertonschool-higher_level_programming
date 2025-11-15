#!/usr/bin/python
for i in range(100):
    if i < 10:
        print(f"{i:02d}", end=", ")
    elif i == 99:
        print(i, end="")
    else:
        print(i, end=", ")
