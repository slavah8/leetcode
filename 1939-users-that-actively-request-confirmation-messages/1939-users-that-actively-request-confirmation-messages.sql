# Write your MySQL query statement below

WITH cte AS (
    SELECT
        user_id,
        time_stamp,
        LAG(time_stamp) OVER (
            PARTITION BY user_id
            ORDER BY time_stamp
        ) AS prev_ts
    FROM Confirmations
)

SELECT DISTINCT(user_id)
FROM cte
WHERE prev_ts is NOT NULL AND TIMESTAMPDIFF(SECOND, prev_ts, time_stamp) <= 24 * 60 * 60
ORDER BY user_id ASC

