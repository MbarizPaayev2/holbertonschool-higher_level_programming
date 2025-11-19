#!/usr/bin/python3
def multiple_returns(sentence):
    li = len(sentence)
    f = sentence[0]
    if f == "":
        return None
    return li, f
