-- TASK 11: List all records with score >= 10 from 'second_table'

-- This query selects score and name from all rows where score is greater than or equal to 10
-- Results are sorted in descending order of score

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;