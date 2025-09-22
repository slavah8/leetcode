# Write your MySQL query statement below
WITH new_table AS (
SELECT p.project_id, ROUND(SUM(experience_years) / COUNT(p.project_id), 2) as average_years
FROM Employee e
JOIN Project p
ON e.employee_id = p.employee_id
GROUP BY p.project_id
)

SELECT *
FROM new_table



