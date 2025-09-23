
SELECT e.employee_id
FROM Employees e
WHERE salary < 30000 AND e.manager_id IS NOT NULL AND e.manager_id NOT IN (
    SELECT e2.employee_id
    FROM Employees e2
)
ORDER BY e.employee_id