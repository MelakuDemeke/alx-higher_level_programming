-- This script lists all records of the `second_table`, ordered by score

-- Use the SELECT statement to retrieve the score and name columns from the second_table
SELECT score, name
-- Specify the table to retrieve data from using the FROM clause
FROM second_table
-- Sort the results by score in descending order using the ORDER BY clause
ORDER BY score DESC;
