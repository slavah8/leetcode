# Write your MySQL query statement below

WITH RECURSIVE cal(d) AS (
    SELECT DATE('2019-01-01')
    UNION ALL
    SELECT d + INTERVAL 1 DAY FROM cal
    WHERE d < '2019-12-31'
),
labeled AS (
    SELECT
    c.d,
    CASE
        WHEN f.fail_date IS NOT NULL THEN 'failed'
        WHEN s.success_date IS NOT NULL THEN 'succeeded'
    END AS period_state
    FROM cal c
    LEFT JOIN Failed f ON f.fail_date = c.d
    LEFT JOIN Succeeded s ON s.success_date = c.d
),
runs AS (
    SELECT
    d,
    period_state,
    DATE_SUB(d, INTERVAL ROW_NUMBER() OVER (
        PARTITION BY period_state
        ORDER BY d
    ) DAY) AS grp_key
    FROM labeled
    WHERE period_state IS NOT NULL
)

SELECT period_state, MIN(d) AS start_date, MAX(d) AS end_date 
FROM runs
GROUP BY period_state, grp_key
ORDER BY start_date

