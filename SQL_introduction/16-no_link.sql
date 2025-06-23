-- TASK 16: List all records with a non-empty name from 'second_table'

-- This query selects only rows where the 'name' column contains a value
-- Only the columns 'score' and 'name' are displayed
-- Results are ordered by score in descending order

SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;