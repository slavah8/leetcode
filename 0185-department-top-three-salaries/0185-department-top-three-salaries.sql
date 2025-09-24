# Write your MySQL query statement below

SELECT d.name AS Department, e.name As Employee, e.salary AS Salary
FROM (
    SELECT
    id,
    name,
    salary,
    departmentId,
    DENSE_RANK() OVER (
        PARTITION BY departmentId
        ORDER BY salary DESC
    ) AS rk
    FROM Employee
) e
JOIN Department d
  ON d.id = e.departmentId
WHERE e.rk <= 3;