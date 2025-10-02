# Write your MySQL query statement below
SELECT
t1.N,
CASE
    WHEN t1.P IS NULL THEN 'Root'
    WHEN COUNT(t2.N) = 0 THEN 'Leaf'
    ELSE 'Inner'
    END AS Type
FROM Tree t1
LEFT JOIN Tree t2
  ON t1.N = t2.P
GROUP BY t1.N, t1.P
ORDER BY t1.N 

  