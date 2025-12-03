#!/usr/bin/python3
"""this is docstr"""
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(i.get("title"))
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
       d = response.json()
       for i in d:
           dict  = {
                   "id": i.get("id")
                   "title":i.get("title")
                   "body":i.get("body")
                }

    with open("posts.csv", "w", encoding ="utf-8") as f:
            reader = csv.DictWriter(f, field = ["id","title","body"])
            reader.writeheader()
            


