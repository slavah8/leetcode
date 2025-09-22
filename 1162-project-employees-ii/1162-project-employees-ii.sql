# Write your MySQL query statement below
WITH counts AS (
SELECT p.project_id , COUNT(*) as emp_count
FROM Project p
GROUP BY p.project_id
),
max_count AS (
SELECT MAX(emp_count) AS mx
FROM counts
)

SELECT c.project_Id
FROM counts c
JOIN max_count m
ON m.mx = c.emp_count

