#!/usr/bin/python3
def islower(c):
    num = ord(c)
    if num > 97 and num < 122:
       return True
    else:
        return False

char = input()
if islower == True:
    print("{}".format(char), "is lower")
else:
    print("{}".format(char), "is upper")
