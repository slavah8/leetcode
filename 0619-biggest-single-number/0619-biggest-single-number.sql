# Write your MySQL query statement below
WITH one_nums AS (
SELECT num
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1
)

SELECT MAX(num) AS num
FROM one_nums
