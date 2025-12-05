#!/usr/bin/python3
from flask import Flask, render_template
import os 
import json 

app = Flask(__name__)

@app.route("/items")
def items():


