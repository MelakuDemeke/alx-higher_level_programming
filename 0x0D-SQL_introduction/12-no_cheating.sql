-- This script updates the score of Bob to 10 in the `second_table`

-- Use the UPDATE statement to modify the score column in the second_table
UPDATE second_table
-- Set the score value to 10 using the SET clause
SET score = 10
-- Specify the condition that the name should be 'Bob' using the WHERE clause
WHERE name = 'Bob';
