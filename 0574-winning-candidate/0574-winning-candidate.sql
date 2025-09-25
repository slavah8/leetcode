# Write your MySQL query statement below
WITH vote_count AS (
SELECT candidateId, COUNT(*) AS votes
FROM Vote
GROUP BY candidateId
)

SELECT name
FROM vote_count v
JOIN Candidate c
  ON v.candidateId = c.id
ORDER BY v.votes DESC
LIMIT 1
