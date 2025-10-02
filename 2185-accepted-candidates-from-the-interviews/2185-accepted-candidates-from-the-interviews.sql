# Write your MySQL query statement below

WITH sum_scores AS (
    SELECT
    interview_id,
    SUM(score) AS interview_score
    FROM Rounds r
    GROUP BY interview_id
)


SELECT c.candidate_id
FROM Candidates c
JOIN sum_scores s
  ON c.interview_id = s.interview_id
WHERE s.interview_score > 15 AND c.years_of_exp >= 2