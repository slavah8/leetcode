# Write your MySQL query statement below

WITH daily AS (
    SELECT
    gender,
    day,
    SUM(score_points) AS day_points
    FROM Scores
    GROUP BY gender, day
)
SELECT
gender,
day,
SUM(day_points) OVER (
    PARTITION BY gender
    ORDER BY day
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS total
FROM daily
ORDER BY gender, day