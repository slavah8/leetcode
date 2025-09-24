# Write your MySQL query statement below

WITH RECURSIVE up AS (
    SELECT employee_id, manager_id
    FROM Employees
    WHERE employee_id <> 1

    UNION
    
    SELECT u.employee_id, e.manager_id
    FROM up u
    JOIN Employees e
      ON u.manager_id = e.employee_id
    WHERE u.manager_id <> 1

)
SELECT DISTINCT employee_id
FROM up
WHERE manager_id = 1
