#!/usr/bin/python3
"""this is docstring"""
import json 


def load_from_json_file(filename):
    """this is docstr"""
    with open(filename, "w", encoding="utf-8") as json_file:
        return json.load(json_file)
