# Write your MySQL query statement below

WITH max_grade AS (
SELECT student_id, MAX(grade) as mx
FROM Enrollments
GROUP BY student_id
), 
chosen_course AS (
    SELECT e.student_id, MIN(course_id) AS min_course
    FROM Enrollments e
    JOIN max_grade m
    ON e.student_id = m.student_id AND m.mx = e.grade
    GROUP BY e.student_id
)

SELECT e.student_id, e.course_id, e.grade
FROM Enrollments e
JOIN chosen_course c
ON e.course_id = c.min_course AND e.student_id = c.student_id
ORDER BY e.student_id ASC