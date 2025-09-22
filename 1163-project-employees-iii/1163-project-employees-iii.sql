WITH joined AS (
    SELECT p.project_id, e.employee_id, e.experience_years
    FROM project p
    JOIN Employee e
    ON e.employee_id = p.employee_id
),
max_per_project AS (
    SELECT project_id, MAX(experience_years) AS max_exp
    FROM joined
    GROUP BY project_id
)

SELECT j.project_id, j.employee_id
FROM joined j
JOIN max_per_project m
ON j.project_id = m.project_id AND j.experience_years = m.max_exp