# Write your MySQL query statement below
WITH totals AS (
    SELECT
    sum(frequency) AS total
    FROM Numbers
),
runs AS (
    SELECT
    num,
    frequency,
    SUM(frequency) OVER (
        ORDER BY num
    ) AS cume,
    SUM(frequency) OVER (ORDER BY num) - frequency AS cume_prev
    FROM Numbers
),
bounds AS (
    SELECT (total + 1) DIV 2 AS left_pos, (total + 2) DIV 2 AS right_pos
    FROM totals
),
picks AS (
    SELECT r.num
    FROM bounds b 
    CROSS JOIN runs r
    WHERE b.left_pos BETWEEN r.cume_prev + 1 AND r.cume

    UNION ALL
    SELECT r.num
    FROM bounds b
    CROSS JOIN runs r
    WHERE b.right_pos BETWEEN r.cume_prev + 1 AND r.cume
)
SELECT ROUND(AVG(num), 1) AS median
FROM picks

