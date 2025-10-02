# Write your MySQL query statement below

WITH RECURSIVE seq(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM seq WHERE n < 20
)


SELECT t.task_id, s.n AS subtask_id
FROM Tasks t
JOIN seq s
  ON s.n <= t.subtasks_count
LEFT JOIN Executed e
  ON e.task_id = t.task_id
  AND e.subtask_id = s.n
WHERE e.task_id IS NULL
ORDER BY t.task_id, subtask_id