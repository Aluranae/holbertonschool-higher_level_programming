-- TASK 4: Create the table 'first_table' with columns 'id' and 'name'

-- This query creates the table only if it doesn't already exist

CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);