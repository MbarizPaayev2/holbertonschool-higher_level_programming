#!/usr/bin/python3
"""this is docstring"""
import json


def save_to_json_file(my_obj, filename):
    """this is also docstr"""
    json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(my_obj)
