# SQL - Introduction

This project is part of the second trimester curriculum at Holberton School. Its goal is to introduce fundamental SQL concepts using MySQL 8.0, including database manipulation, table creation, data insertion, selection, aggregation, and filtering using basic SQL statements.

All tasks are executed using SQL scripts run from the command line with a provided database name.

## Project Objectives

- Understand and manipulate MySQL databases and tables.
- Execute basic SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
- Use SQL clauses such as `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`.
- Work with functions like `COUNT`, `AVG`, `MAX`, `MIN`.
- Ensure scripts do not fail if objects already exist.
- Write clean, readable SQL using uppercase keywords and consistent formatting.

## Tasks Overview

| Task | File | Description |
|------|------|-------------|
| 0 | `0-list_databases.sql` | List all databases on the MySQL server |
| 1 | `1-create_database_if_missing.sql` | Create a database only if it doesn't exist |
| 2 | `2-remove_database.sql` | Delete a database if it exists |
| 3 | `3-list_tables.sql` | List all tables in a given database |
| 4 | `4-first_table.sql` | Create a table with two fields: `id`, `name` |
| 5 | `5-full_table.sql` | Show full creation SQL for a table without using DESCRIBE |
| 6 | `6-list_values.sql` | Select all records from a table |
| 7 | `7-insert_value.sql` | Insert one new record into a table |
| 8 | `8-count_89.sql` | Count how many rows have `id = 89` |
| 9 | `9-full_creation.sql` | Create a new table and insert multiple records |
| 10 | `10-top_score.sql` | List all records ordered by highest `score` |
| 11 | `11-best_score.sql` | List all records with `score >= 10`, ordered by score |
| 12 | `12-no_cheating.sql` | Update the score of `Bob` to 10 without using his ID |
| 13 | `13-change_class.sql` | Delete all records with `score <= 5` |
| 14 | `14-average.sql` | Compute the average score of all records |
| 15 | `15-groups.sql` | Count how many records exist per score and sort by count |
| 16 | `16-no_link.sql` | List all records with a non-empty name field, ordered by score |

## Usage

Each script should be executed as follows:

```bash
cat [filename].sql | mysql -hlocalhost -uroot -p [database_name]
```

## Author

Project done as part of Holberton School curriculum.