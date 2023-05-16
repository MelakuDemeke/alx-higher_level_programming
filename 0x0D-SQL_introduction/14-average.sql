-- This query computes the average score of all records in the `second_table` table of the `hbtn_0c_0` database.

-- The SELECT statement calculates the average using the AVG() function on the `score` column, and assigns the result to the column alias `average`.
SELECT AVG(score) AS average
FROM second_table;
