-- This script lists all records with a score >= 10 in the `second_table`

-- Use the SELECT statement to retrieve the score and name columns from the second_table
SELECT score, name
-- Specify the table to retrieve data from using the FROM clause
FROM second_table
-- Specify the condition that the score should be greater than or equal to 10 using the WHERE clause
WHERE score >= 10
-- Sort the results by score in descending order using the ORDER BY clause
ORDER BY score DESC;
