# Write your MySQL query statement below

WITH totals AS (
    SELECT
      s.user_id,
      p.product_id,
      SUM(s.quantity * p.price) AS total_spend
    FROM Sales s
    JOIN Product p ON s.product_id = p.product_id
    GROUP BY s.user_id, p.product_id
),
max_per_user AS (
    SELECT user_id, max(total_spend) AS max_spend
    FROM totals
    GROUP BY user_id
)
SELECT m.user_id, t.product_id
FROM totals t
JOIN max_per_user m
    ON m.user_id = t.user_id
    AND m.max_spend = t.total_spend;
