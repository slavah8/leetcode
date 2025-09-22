# Write your MySQL query statement below
WITH manager_count AS (
    SELECT
    managerId,
    COUNT(*) as count
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
)
SELECT e.name as name
FROM manager_count m
JOIN Employee e
ON m.managerId = e.id
WHERE m.count >= 5