# Write your MySQL query statement below
WITH first_devices AS (
SELECT
player_id,
device_id,
event_date,
games_played,
ROW_NUMBER() OVER (
    PARTITION BY player_id
    ORDER BY event_date
) AS rn
FROM Activity
)

SELECT
player_id,
device_id
FROM first_devices
WHERE rn = 1