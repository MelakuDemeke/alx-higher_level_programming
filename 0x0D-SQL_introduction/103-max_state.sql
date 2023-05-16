-- Select the state column and the max value column, and alias the max value column as max_temp.
SELECT state, MAX(value) AS max_temp
-- From the temperatures table.
FROM temperatures
-- Group the results by state.
GROUP BY state
-- Order the results by state name.
ORDER BY state;
