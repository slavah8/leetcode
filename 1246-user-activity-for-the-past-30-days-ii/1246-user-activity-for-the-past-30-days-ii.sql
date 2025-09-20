# Write your MySQL query statement below
# sessions // users

WITH per_user AS (
    SELECT user_id, COUNT(DISTINCT session_id) AS sessions
    FROM Activity
    WHERE DATEDIFF('2019-07-27', activity_date) BETWEEN 0 AND 29
    GROUP BY user_id
)
SELECT ROUND(IFNULL(AVG(sessions), 0), 2) AS average_sessions_per_user
FROM per_user
