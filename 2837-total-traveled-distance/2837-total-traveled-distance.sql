# Write your MySQL query statement below
WITH totals AS (
    SELECT
    user_id,
    SUM(distance) AS total_distance
FROM Rides
GROUP BY user_id
)

SELECT
    u.user_id,
    u.name,
    COALESCE(t.total_distance, 0) AS 'traveled distance'
FROM Users u
LEFT JOIN totals t
  ON t.user_id = u.user_id
ORDER BY u.user_id ASC
