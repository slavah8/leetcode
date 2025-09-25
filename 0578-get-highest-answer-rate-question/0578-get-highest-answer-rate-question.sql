# Write your MySQL query statement below
SELECT question_id AS survey_log
FROM (
SELECT
question_id,
SUM(action = 'answer') AS answers,
SUM(action = 'show') AS shows,
SUM(action = 'answer') / SUM(action = 'show') AS rate
FROM SurveyLog
GROUP BY question_id
) q
WHERE q.shows > 0
ORDER BY q.rate DESC, q.question_id ASC
LIMIT 1