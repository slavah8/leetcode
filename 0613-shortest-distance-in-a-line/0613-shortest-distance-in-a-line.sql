# Write your MySQL query statement below
SELECT MIN(diff) AS shortest
FROM (
    SELECT ABS(x - LEAD(x) OVER (ORDER BY x)) AS diff
    FROM Point
) AS t
WHERE diff IS NOT NULL;
