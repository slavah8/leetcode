# Write your MySQL query statement below
WITH distances AS (
    SELECT
    user_id,
    SUM(distance) AS total_traveled
    FROM Rides
    GROUP BY user_id
)

SELECT 
    u.name AS name,
    COALESCE(d.total_traveled, 0) AS travelled_distance
FROM Users u
LEFT JOIN distances d
  ON d.user_id = u.id
ORDER BY travelled_distance DESC, name ASC;
