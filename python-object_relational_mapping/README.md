# Python - Object-relational mapping

This project is part of the second trimester at Holberton School and aims to introduce students to the fundamental concepts of Object-Relational Mapping (ORM) using **MySQL**, **MySQLdb**, and **SQLAlchemy**.

It gradually transitions from direct SQL queries with `MySQLdb` to more abstracted, object-oriented manipulation using `SQLAlchemy`.

---

## 📚 Learning Objectives

- Understand what ORM is and how it works.
- Interact with MySQL databases using both MySQLdb and SQLAlchemy.
- Perform SELECT, INSERT, UPDATE, DELETE operations using Python code.
- Define Python classes mapped to database tables using declarative_base().
- Prevent SQL injections by using parameterized queries or ORM filters.
- Execute joins and sort data via SQLAlchemy syntax.

---

## 🧪 Technologies

- Language: Python 3.8+
- ORM: SQLAlchemy (>=1.4.x or 2.x)
- MySQL Server: 5.7+
- OS: Ubuntu 20.04 LTS (or compatible)
- MySQLdb (mysqlclient) for low-level MySQL access

---

## 🚀 Tasks Overview

| Task | Filename | Description |
|------|----------|-------------|
| 0. Select states | `0-select_states.py` | Lists all states from the database using MySQLdb |
| 1. Filter states | `1-filter_states.py` | Filters states starting with 'N' |
| 2. Filter by user input | `2-my_filter_states.py` | Filters states by exact name (unsafe) |
| 3. Safe from SQL injection | `3-my_safe_filter_states.py` | Secures user input from SQL injection |
| 4. Cities by state | `4-cities_by_state.py` | Lists all cities with their state id |
| 5. Filter cities | `5-filter_cities.py` | Lists all cities of a given state |
| 6. Model state | `6-model_state.py` | Defines a State class using SQLAlchemy |
| 7. Fetch all states | `7-model_state_fetch_all.py` | Displays all `State` objects |
| 8. Fetch first state | `8-model_state_fetch_first.py` | Displays first state (ordered by ID) |
| 9. Filter with 'a' | `9-model_state_filter_a.py` | Lists states whose name contains 'a' |
| 10. Search by name | `10-model_state_my_get.py` | Gets state by name or shows 'Not found' |
| 11. Insert state | `11-model_state_insert.py` | Adds a new state ("Louisiana") |
| 12. Update state | `12-model_state_update_id_2.py` | Changes the name of state with ID 2 |
| 13. Delete states | `13-model_state_delete_a.py` | Deletes all states containing 'a' |
| 14. Cities by State | `14-model_city_fetch_by_state.py` | Uses `City` and `State` classes to show city info |

---

## 🧠 Tips

- Always close your cursor and database connection (`cursor.close()`, `db.close()`).
- Ensure that your SQLAlchemy models are declared **before** calling `Base.metadata.create_all(engine)`.
- Use `filter_by()` and `filter()` correctly to avoid fetching all rows unnecessarily.
- Don’t forget to commit changes (`session.commit()`) when modifying the database.

---

## ✅ Expected Format

All results are printed exactly as required:
- Tuples for raw MySQLdb outputs.
- String formatting (e.g. `1: California`) for SQLAlchemy object queries.
- Proper order is always maintained (`ORDER BY id ASC` or `.order_by(Model.id)`).

---

Project done as part of Holberton School curriculum
