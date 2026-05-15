# Write your MySQL query statement below
WITH free AS (
    SELECT
    user_id,
    activity_type,
    ROUND(AVG(activity_duration), 2) AS trial_avg_duration
    FROM UserActivity
    WHERE activity_type = 'free_trial'
    GROUP BY user_id, activity_type
),
paid AS (
    SELECT
    user_id,
    activity_type,
    ROUND(AVG(activity_duration), 2) AS paid_avg_duration
    FROM UserActivity
    WHERE activity_type = 'paid'
    GROUP BY user_id, activity_type
)

SELECT
f.user_id,
f.trial_avg_duration,
p.paid_avg_duration
FROM free AS f
JOIN paid AS p
  ON f.user_id = p.user_id
ORDER BY f.user_id ASC




