#!/usr/bin/python3


def uppercase(s):
    for i in s:
        num = ord(i)
        if 97 <= num <= 122:
            i = chr(num - 32)
        print("{}".format(i), end="")
    print()


if __name__ == "__main__":
    s = input()
    uppercase(s)
