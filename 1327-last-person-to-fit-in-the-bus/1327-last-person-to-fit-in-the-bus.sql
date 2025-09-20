# Write your MySQL query statement below
WITH c AS (
    SELECT
    person_name,
    turn,
    SUM(weight) OVER (ORDER BY turn) AS running_total
    FROM Queue
)

SELECT person_name 
FROM c
WHERE running_total <= 1000 
ORDER BY running_total DESC
LIMIT 1