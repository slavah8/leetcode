# Write your MySQL query statement below

WITH excellent_ny AS (
    SELECT
        COUNT(*) AS ny
    FROM NewYork
    WHERE score >= 90

),
excellent_cal AS (
    SELECT 
        COUNT(*) AS cal
    FROM California
    WHERE score >= 90
)

SELECT
    CASE WHEN n.ny > c.cal THEN 'New York University'
    WHEN n.ny < c.cal THEN 'California University'
    ELSE 'No Winner'
    END AS winner
FROM excellent_ny n
CROSS JOIN excellent_cal c