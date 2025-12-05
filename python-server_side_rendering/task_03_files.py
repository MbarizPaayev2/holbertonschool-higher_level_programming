#!/usr/bin/python3
from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)


def read_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("products", [])
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []


def read_csv(file_path):
    data = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")

    return data


@app.route("/products")
def products():
    source = request.args.get("source", "json").lower()
    product_id = request.args.get("id")
    error = None
    products_data = []

    if source == "json":
        products_data = read_json("products.json")
    elif source == "csv":
        products_data = read_csv("products.csv")
    else:
        error = "Wrong source"

    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products_data if p["id"] == product_id]
            if not filtered:
                error = "Product not found"
            else:
                products_data = filtered
        except ValueError:
            error = "Invalid id"

    return render_template(
        "product_display.html",
        products=products_data,
        error=error,
        source=source
    )


if __name__ == "__main__":
    app.run(debug=True)

