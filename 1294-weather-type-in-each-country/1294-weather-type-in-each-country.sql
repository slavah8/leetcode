# Write your MySQL query statement below

SELECT
    c.country_name AS country_name,
    CASE
        WHEN  avg_state <= 15 THEN 'Cold'
        WHEN  avg_state >= 25 THEN 'Hot'
        ELSE 'Warm'
    END AS weather_type
FROM (
    SELECT
        country_id,
        AVG(weather_state) AS avg_state
    FROM Weather
    WHERE day BETWEEN '2019-11-01' AND '2019-11-30'
    GROUP BY country_id
) AS w
JOIN Countries AS c
  ON c.country_id = w.country_id;