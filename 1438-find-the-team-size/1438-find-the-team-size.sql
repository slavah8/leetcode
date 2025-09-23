# Write your MySQL query statement below
WITH size AS (
SELECT team_id, COUNT(*) AS team_size
FROM Employee
GROUP BY team_id
) 

SELECT 
e.employee_id,
s.team_size
FROM Employee e
JOIN size s
  ON e.team_id = s.team_id