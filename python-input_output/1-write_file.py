#!/usr/bin/python3
"""this is document"""


def write_file(filename="", text=""):
    """this is document"""
    with open(filename, text, "r", encoding="utf-8") as f:
        return f.count()
