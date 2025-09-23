# Write your MySQL query statement below

WITH managers AS (
SELECT DISTINCT e1.employee_id, e1.name AS manager_name, e1.age
FROM Employees e1
JOIN Employees e2
  ON e1.employee_id = e2.reports_to
),
managers_count AS (
    SELECT e2.reports_to AS manager_id, COUNT(*) AS reports_count
    FROM Employees e2
    GROUP BY e2.reports_to
),
avg_age AS (
    SELECT e2.reports_to AS manager_id, ROUND(AVG(e2.age), 0) AS average_age
    FROM Employees e2
    GROUP BY e2.reports_to
)

SELECT m.employee_id, m.manager_name AS name, mc.reports_count, aa.average_age
FROM managers m
JOIN managers_count mc
  ON mc.manager_id = m.employee_id
JOIN avg_age aa
  ON aa.manager_id = m.employee_id
ORDER BY m.employee_id
  