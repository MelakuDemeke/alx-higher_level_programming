-- Select the city and calculate the average temperature
SELECT city, AVG('value') AS avg_temp
-- From the weather_data table
FROM weather_data
-- Group the results by city
GROUP BY city
-- Order the results by average temperature in Fahrenheit, descending
ORDER BY avg_temp DESC;
