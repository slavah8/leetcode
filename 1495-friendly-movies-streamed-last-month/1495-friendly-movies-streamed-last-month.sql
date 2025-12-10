# Write your MySQL query statement below


WITH cte AS (
    SELECT content_id
    FROM TVProgram
    WHERE YEAR(program_date) = 2020 AND MONTH(program_date) = 6
)

SELECT DISTINCT(c2.title)
FROM cte c1
JOIN Content c2
  ON c1.content_id = c2.content_id
WHERE c2.Kids_content = 'Y' AND c2.content_type = 'Movies'
