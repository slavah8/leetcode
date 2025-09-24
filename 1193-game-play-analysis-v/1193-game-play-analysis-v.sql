# Write your MySQL query statement below
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
)

SELECT
f.install_dt,
COUNT(*) AS installs,
ROUND(
    AVG(CASE WHEN a.player_id IS NOT NULL THEN 1 ELSE 0 END), 2
) AS Day1_retention
FROM first_login f
LEFT JOIN Activity a
  ON f.player_id = a.player_id AND a.event_date = DATE_ADD(f.install_dt, INTERVAL 1 DAY)
GROUP BY f.install_dt
