#!/usr/bin/python3

def uppercase(s):
    res = ""
    for i in s:
        num = ord(i)
        if 97 < = num < = 122:
            res = res + chr(num - 32)
        else:
            res = res + i
    return res


if __name__ = "__main__":
    s = input()
print("{}".format(uppercase(s)))
