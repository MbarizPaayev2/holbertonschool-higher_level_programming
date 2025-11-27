#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    json.dump(filename, data)
    pass

def load_and_deserialize(filename):
    json.load(filename)
    pass
