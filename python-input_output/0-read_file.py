#!/usr/bin/python3
"""this is document for this task"""


def read_file(filename=""):
    """this is class docstring"""
    with open(filename, "r", encoding="utf-8") as f:
        cont = f.read()
        return cont
