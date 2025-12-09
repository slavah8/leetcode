# Write your MySQL query statement below

WITH monthly_spending AS (
    SELECT
    o.customer_id,
    DATE_FORMAT(o.order_date, '%Y-%m') AS ym,
    SUM(o.quantity * p.price) AS total_spent
    FROM Orders o
    LEFT JOIN Product p
      ON o.product_id = p.product_id
    WHERE o.order_date BETWEEN '2020-06-01' AND '2020-07-31'
    GROUP BY o.customer_id, ym
)

SELECT c.customer_id, c.name
FROM monthly_spending m
JOIN Customers c
  ON m.customer_id = c.customer_id
WHERE m.total_spent >= 100 AND m.ym IN ('2020-06', '2020-07')
GROUP BY c.customer_id, c.name
HAVING COUNT(DISTINCT m.ym) = 2;