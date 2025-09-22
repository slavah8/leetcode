# Write your MySQL query statement below

WITH per_team AS (
    SELECT
    host_team AS team_id,
    CASE
      WHEN host_goals > guest_goals THEN 3
      WHEN host_goals = guest_goals THEN 1
      ELSE 0
    END AS pts
    FROM MATCHES
    UNION ALL
    SELECT guest_team AS team_id,
    CASE
      WHEN guest_goals > host_goals THEN 3
      WHEN guest_goals = host_goals THEN 1
      ELSE 0
    END AS pts
    FROM Matches
),

totals AS (
SELECT team_id, SUM(pts) AS num_points
FROM per_team
GROUP BY team_id
)

SELECT t.team_id, t.team_name, COALESCE(s.num_points, 0) AS num_points
FROM Teams t
LEFT JOIN totals s
ON t.team_id = s.team_id
ORDER BY num_points DESC, t.team_id ASC
