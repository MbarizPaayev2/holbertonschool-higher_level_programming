#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r") as f:
        cont = f.read()
        return cont
