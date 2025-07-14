#!/usr/bin/env python3
"""
Flask route that reads a list of items from a JSON file
and renders them using a dynamic Jinja template with loop and condition.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    file = "items.json"
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        items_list = data.get("items", [])
    return render_template("items.html", items=items_list)


@app.route('/products')
def products():

    source = request.args.get("source", "").lower()
    products = []
    error = None

    try:
        if source == "json":
            with open("products.json", "r", encoding="utf-8") as f:
                products = json.load(f)
        elif source == "csv":
            with open("products.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                products = list(reader)

        elif source == "sql":
            try:
                conn = sqlite3.connect("products.db")
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT id, name, category, price FROM Products"
                )
                rows = cursor.fetchall()

                products = []
                for row in rows:
                    product = {
                        "id": row[0],
                        "name": row[1],
                        "category": row[2],
                        "price": row[3]
                    }
                    products.append(product)

                conn.close()
            except Exception as e:
                error = "Erreur lors de l'accès " \
                    "à la base de données : {}".format(e)

        else:
            error = "Wrong source"
    except Exception as e:
        error = "Erreur lors du chargement des données : {}".format(e)

    # Bloc de filtrage par ID
    product_id = request.args.get("id")

    if product_id and not error:
        try:
            product_id = int(product_id)

            found = None
            for product in products:
                product_id_value = int(product["id"]) \
                    if isinstance(product["id"], str) else product["id"]
                if product_id_value == product_id:
                    found = product
                    break

            if found:
                products = [found]
            else:
                error = "Product not found"
                products = []

        except ValueError:
            error = "Invalid ID format. Must be a number."
            products = []

    return render_template(
        "product_display.html",
        products=products,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
