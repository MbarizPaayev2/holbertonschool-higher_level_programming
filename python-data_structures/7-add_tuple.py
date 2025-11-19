#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = str(tuple_a)
    new1 = str(tuple_b)
    return (new[0] + new1[0], new[1] + new1[1])
    
def str(t=()):
    if len(t) == 2:
        n = t[0],t[1]
    elif len(t) < 2:
        n = t[0],0
    elif len(t) > 2:
        n = t[0],t[1]
    return n;     
