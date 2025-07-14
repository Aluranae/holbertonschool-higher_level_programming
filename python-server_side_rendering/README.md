# Flask Project – Server-Side Rendering with JSON, CSV and SQLite

## 📚 Project Overview

This mini-project demonstrates how to build a dynamic Flask application that renders HTML templates using server-side rendering techniques. Throughout the 5 tasks, students progressively learn to integrate static and dynamic data using Jinja2 templates, Flask routes, and data retrieved from various sources including JSON files, CSV files, and a SQLite database.

---

## 🎯 Learning Objectives

- Understand the principles of server-side rendering with Flask and Jinja2.
- Create reusable HTML templates using `{% include %}` blocks.
- Dynamically inject data into templates using loops and conditionals.
- Parse and manipulate data from JSON and CSV files.
- Connect to and retrieve data from a SQLite database.
- Handle query parameters and errors in Flask routes.

---

## 📌 Tasks Breakdown

### ✅ Task 0: Introduction to Jinja Templates
- Create a Flask app that serves three pages (`index`, `about`, and `contact`).
- Use `{% include %}` to reuse `header.html` and `footer.html` in each page.
- Serve static HTML pages with a consistent layout.

---

### ✅ Task 1: Dynamic Content with Jinja
- Extend the app with a route `/items`.
- Load data from a `items.json` file.
- Use `{% for %}` loop and `{% if %}` conditionals in `items.html` to render an unordered list.
- Display a fallback message if the list is empty.

---

### ✅ Task 2: Conditional Rendering and Template Reuse
- Refactor and unify all HTML templates.
- Ensure `header.html` contains navigation links to all valid routes, including `/items`.
- All templates include both `header` and `footer`.

---

### ✅ Task 3: Display Products from JSON or CSV
- Create a dynamic route `/products` that accepts a `source` parameter (`json` or `csv`) and optional `id` parameter.
- Parse product data from `products.json` or `products.csv`.
- Display the data in a table using `product_display.html`.
- Handle edge cases:
  - If `source` is invalid → show "Wrong source"
  - If `id` not found → show "Product not found"

---

### ✅ Task 4: Add SQLite Support
- Extend `/products` route to also support `source=sql`.
- Use `sqlite3` to connect to a local database `products.db`.
- Fetch data from the `Products` table and render using the same template.
- Maintain support for optional `id` filtering.
- Handle database errors and invalid inputs gracefully.

---

## 🧪 Example Queries

```bash
# Display all products from JSON
http://localhost:5000/products?source=json

# Filter a product by ID from CSV
http://localhost:5000/products?source=csv&id=2

# Attempt with an invalid source
http://localhost:5000/products?source=xml

# Display products from SQLite
http://localhost:5000/products?source=sql
```

---

## ✅ Validation

Each task was tested with multiple edge cases (empty list, invalid query, non-existent ID) to ensure robust error handling and consistent rendering.