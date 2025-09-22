# Write your MySQL query statement below

WITH first_login AS (
    SELECT MIN(activity_date) AS first_login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
)
SELECT first_login_date AS login_date, COUNT(*) AS user_count
FROM first_login
WHERE DATEDIFF('2019-06-30', first_login_date) BETWEEN 0 AND 90
GROUP BY first_login_date

