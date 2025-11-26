#!/usr/bin/python3
"""this is docstring"""
import json 


def load_from_json_file(filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        return json.loads(filename)
