# Write your MySQL query statement below
WITH t1 AS (
    SELECT
    id,
    company,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY company
        ORDER BY salary, id
    ) AS rn,
    COUNT(*) OVER (
        PARTITION BY company
    ) AS cnt
    FROM Employee
)

SELECT id, company, salary
FROM t1
WHERE rn BETWEEN (cnt + 1) DIV 2 AND (cnt + 2) / 2 
