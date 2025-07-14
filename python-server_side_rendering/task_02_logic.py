#!/usr/bin/env python3
"""
Flask route that reads a list of items from a JSON file
and renders them using a dynamic Jinja template with loop and condition.
"""

from flask import Flask, render_template
import json

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
