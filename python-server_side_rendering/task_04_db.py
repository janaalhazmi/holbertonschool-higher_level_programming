#!/usr/bin/python3
"""Flask application for displaying products from JSON, CSV, or SQL."""

from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    """Read products from CSV file."""
    with open("products.csv", "r") as file:
        return list(csv.DictReader(file))


def read_sql():
    """Read products from SQLite database."""
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, category, price FROM Products"
    )

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products


@app.route("/products")
def products():
    """Display products from JSON, CSV, or SQL."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    try:
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        else:
            data = read_sql()

    except (sqlite3.Error, OSError, json.JSONDecodeError):
        return render_template(
            "product_display.html",
            error="Database error"
        )

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