#!/usr/bin/python3
from flask import Flask, render_template
import os 
import json 

app = Flask(__name__)

@app.route("/items")
def items():
    item = []

    json_file = 'items.html'
    if os.path.exists(json_file):
        try:
            with open(json_file, "r") as f:
                file = json.load(f)
                items = file.get('items.html', [])
        except Exception as e :
                print(f"Error reading JSON file: {e}")
    else:
        print(f"{json_file} not found.")
return render_template('items.html', items=items_list)

if __name__ == "__main__":
    app.run()
