-- Displays the top 3 cities by average temperature during July and August, ordered by temperature descending

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;