-- Count the number of records with the same score and label it as 'number'
SELECT score, COUNT(*) AS number
FROM second_table
-- Group the results by score
GROUP BY score
-- Order the results by the number of records in descending order
ORDER BY number DESC;
