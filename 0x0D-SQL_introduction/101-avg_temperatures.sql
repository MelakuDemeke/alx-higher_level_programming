-- Select the city and calculate the average temperature
SELECT `city`, AVG(`value`) AS `avg_temp`
-- From the temperatures table
FROM `temperatures`
-- Group the results by city
GROUP BY `city`
-- Order the results by average temperature in Fahrenheit, descending
ORDER BY `avg_temp` DESC;
