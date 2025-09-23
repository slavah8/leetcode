# Write your MySQL query statement below
WITH flags AS (
    SELECT log_id, 
    CASE WHEN LAG(log_id) OVER (ORDER BY log_id) = log_id - 1 THEN 0 ELSE 1 END AS is_start
    FROM Logs
),
grps AS (
    SELECT 
      log_id,
      SUM(is_start) OVER (ORDER BY log_id) AS g
    FROM flags
)


SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM grps
GROUP BY g