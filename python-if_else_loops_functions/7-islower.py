#!/usr/bin/python3


def islower(c):
    num = ord(c)
    if 97 <= num <= 122:
        return True
    return False


if __name__ == "__main__":
    char = input()
    if islower(char):
        print("{} => lower".format(char))
    else:
        print("{} => upper".format(char))
