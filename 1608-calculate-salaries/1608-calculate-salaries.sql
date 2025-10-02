# Write your MySQL query statement below

WITH max_salary AS (
    SELECT company_id, MAX(salary) AS maxx
    FROM Salaries
    GROUP BY company_id
)

SELECT
s.company_id,
s.employee_id,
s.employee_name,
CASE
    WHEN m.maxx < 1000 THEN ROUND(salary, 0)
    WHEN m.maxx BETWEEN 1000 AND 10000 THEN ROUND(salary * .76, 0)
    WHEN m.maxx > 10000 THEN ROUND(salary * .51, 0)
END AS salary
FROM Salaries s
JOIN max_salary m
ON s.company_id = m.company_id
