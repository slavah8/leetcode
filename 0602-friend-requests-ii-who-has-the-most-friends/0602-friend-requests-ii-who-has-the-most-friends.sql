# Write your MySQL query statement below
WITH edges AS (
    SELECT requester_id AS id, accepter_id AS friend
    FROM RequestAccepted
    
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend
    FROM RequestAccepted
),
counts AS (
    SELECT id, COUNT(DISTINCT friend) AS num
    FROM edges
    GROUP BY id
),
maxnum AS (
    SELECT MAX(num) AS mx
    FROM counts
)
SELECT c.id, c.num
FROM counts c
JOIN maxnum m
    ON c.num = m.mx;