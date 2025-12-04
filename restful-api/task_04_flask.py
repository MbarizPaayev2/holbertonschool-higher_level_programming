#!/usr/bin/python3
"""this is docs"""
from flask import Flask
from flask import jsonify

app = Flask(__name__) 
@app.route("/")
def home():
     return "<p>Welcome to the Flask API</p>"
if __name__ == "__main__":
    app.run()
