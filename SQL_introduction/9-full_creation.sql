-- TASK 9: Create 'second_table' and insert multiple records

-- This script creates a table with 3 columns and inserts 4 predefined rows

CREATE table IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);