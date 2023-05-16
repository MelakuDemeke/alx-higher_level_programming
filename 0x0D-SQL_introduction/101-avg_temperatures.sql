-- Select the city and calculate the average temperature in Fahrenheit, rounding to 2 decimal places
SELECT city, ROUND(AVG((temperature * 9/5) + 32), 2) AS avg_temp_f
-- From the weather_data table
FROM weather_data
-- Group the results by city
GROUP BY city
-- Order the results by average temperature in Fahrenheit, descending
ORDER BY avg_temp_f DESC;
