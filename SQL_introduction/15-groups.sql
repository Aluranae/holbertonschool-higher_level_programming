-- TASK 15: Count how many records have each score in 'second_table'

-- This query groups records by score and counts how many times each score appears
-- Results are ordered by the number of records per score, from most to least
-- The count column must be labeled 'number'

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;