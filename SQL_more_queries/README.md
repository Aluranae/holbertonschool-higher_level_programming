# SQL - More Queries

## 📚 Description

This project builds upon the foundations laid in “SQL - Introduction”. You will go further in writing SQL queries, using `JOIN`, `SUBQUERY`, `FOREIGN KEY`, `GROUP BY`, `HAVING`, `COUNT`, and more complex logic.

It introduces the relational nature of SQL databases and how multiple tables can be linked together efficiently. You will also learn about constraints like uniqueness, not-null, default values, and how to import/export data with SQL dump files.

---

## 🧠 Learning Objectives

- How to create new users in MySQL
- How to manage privileges for a MySQL user
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve data from multiple tables using `JOIN` and `LEFT JOIN`
- How to use subqueries within queries
- How to use MySQL functions like `COUNT()`, `GROUP BY`, `HAVING`
- How to import a `.sql` dump

---

## ⚙️ Environment

- Ubuntu 20.04 LTS
- MySQL 8.0+
- SQL scripts tested with: `cat [file] | mysql -hlocalhost -uroot -p [database]`

---

## 📌 Project Tasks

### 0. My privileges!
Display all privileges for the current MySQL user.

### 1. Root user
Create the MySQL user `user_0d_1` with all privileges.

### 2. Read user
Create a new user `user_0d_2` and grant only SELECT access.

### 3. Always a name
Create a table `force_name` with a `NOT NULL` `name` column.

### 4. ID not null
Create a table with an `id` column having a default value.

### 5. Unique ID
Create a table with a `UNIQUE` constraint on the `id` column.

### 6. States table
Create the `states` table with an auto-incremented `id` and `name` column.

### 7. Cities table
Create the `cities` table with a foreign key pointing to `states`.

### 8. Cities of California
List all cities in California **without using JOIN**.

### 9. Cities by States
List all cities and their state names using a `JOIN`.

### 10. Genre ID by show
List all shows and associated genre IDs using a single `SELECT`.

### 11. Genre ID for all shows
Same as task 10, but show all shows (even those without genres).

### 12. No genre
List shows without any associated genre (genre is `NULL`).

### 13. Number of shows by genre
Display each genre and how many shows are linked to it.

### 14. My genres
List all genres associated with the show “Dexter”.

### 15. Only Comedy
List all shows associated with the genre “Comedy”.

### 16. List shows and genres
List all shows and all their associated genres (or NULL).

---

## ▶️ Usage

```bash
cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

> Replace the script name and database name as needed for each task.

---

## ✍️ Author

Project completed as part of Holberton School curriculum – 2nd trimester.
