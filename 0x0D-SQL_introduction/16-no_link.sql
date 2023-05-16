-- Selects the score and name columns from the second_table where the name is not null
SELECT score, name FROM second_table WHERE name IS NOT NULL
-- Orders the result by score in descending order
ORDER BY score DESC;
