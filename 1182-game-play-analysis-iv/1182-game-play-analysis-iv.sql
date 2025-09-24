# Write your MySQL query statement below
WITH logins AS (
    SELECT
    player_id,
    device_id,
    games_played,
    event_date,
    ROW_NUMBER() OVER (
        PARTITION BY player_id
        ORDER BY event_date
    ) AS rn
    FROM Activity
),
first_logins AS (
    SELECT
    player_id,
    event_date AS first_login
    FROM logins
    WHERE rn = 1
),
next_day_returners AS (
    SELECT DISTINCT a.player_id
    FROM Activity a
    JOIN first_logins l
      ON a.player_id = l.player_id AND a.event_date = DATE_ADD(l.first_login, INTERVAL 1 DAY)
)

SELECT 
ROUND((SELECT COUNT(*) FROM next_day_returners) 
/ (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction