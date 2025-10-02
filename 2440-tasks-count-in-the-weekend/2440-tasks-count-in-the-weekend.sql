# Write your MySQL query statement below
SELECT
SUM(CASE WHEN WEEKDAY(submit_date) IN (5, 6) THEN 1 ELSE 0 END) AS weekend_cnt,
SUM(CASE WHEN WEEKDAY(submit_date) IN (0,1,2,3,4) THEN 1 ELSE 0 END) AS working_cnt
FROM Tasks
