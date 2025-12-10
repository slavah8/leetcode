# Write your MySQL query statement below

WITH subs_2021 AS (
    SELECT account_id
    FROM Subscriptions
    WHERE start_date <= '2021-12-31'
      AND end_date >= '2021-01-01'
)

SELECT
    COUNT(*) AS accounts_count
FROM subs_2021 s
LEFT JOIN Streams st
  ON s.account_id = st.account_id
  AND st.stream_date BETWEEN '2021-01-01' AND '2021-12-31'
WHERE st.session_id is NULL