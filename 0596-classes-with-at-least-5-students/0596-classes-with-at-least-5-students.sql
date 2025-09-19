# Write your MySQL query statement below
SELECT class as class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5