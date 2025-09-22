# Write your MySQL query statement below
WITH average_activity AS (
    SELECT event_type, AVG(occurrences) AS avg_activity
    FROM Events
    GROUP BY event_type
),
flagged AS (
    SELECT
    e.business_id,
    e.event_type,
    e.occurrences,
    (e.occurrences > a.avg_activity) AS above_avg
    FROM Events e
    JOIN average_activity a
    ON e.event_type = a.event_type
),
per_business AS (
    SELECT business_id, SUM(above_avg) AS count_above
    FROM flagged
    GROUP BY business_id
)

SELECT business_id
FROM per_business
WHERE count_above > 1;