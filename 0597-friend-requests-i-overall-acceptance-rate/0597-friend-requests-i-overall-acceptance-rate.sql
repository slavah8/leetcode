# Write your MySQL query statement below
WITH req AS(
    SELECT COUNT(DISTINCT sender_id, send_to_id) AS total_req
    FROM FriendRequest
),
acc AS (
    SELECT COUNT(DISTINCT requester_id, accepter_id) AS total_acc
    FROM RequestAccepted
)
SELECT
    CASE
        WHEN req.total_req = 0 THEN 0.00
        ELSE ROUND(acc.total_acc / req.total_req, 2)
    END AS accept_rate
FROM req CROSS JOIN acc