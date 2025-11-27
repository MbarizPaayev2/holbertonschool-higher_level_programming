#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding = "utf-8") as f:
        json.dump(f, data)
    pass

def load_and_deserialize(filename):
    json.load(filename)
    pass
