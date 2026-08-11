#!/usr/bin/python3
"""Displaying Data from JSON or CSV Files in Flask"""

from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    """Read products from CSV file."""
    with open("products.csv", "r") as file:
        return list(csv.DictReader(file))


@app.route("/products")
def products():
    """Display products from JSON or CSV."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    if source == "json":
        data = read_json()
    else:
        data = read_csv()

    if product_id:
        products = [
            product for product in data
            if str(product["id"]) == product_id
        ]

        if not products:
            return render_template(
                "product_display.html",
                error="Product not found"
            )
    else:
        products = data

    return render_template(
        "product_display.html",
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)