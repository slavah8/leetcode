# Write your MySQL query statement below
WITH ranked AS (
    SELECT
    customer_id,
    order_id,
    order_date,
    RANK() OVER (
        PARTITION BY customer_id
        ORDER BY order_date DESC
    ) AS rnk
    FROM Orders
)

SELECT
c.name AS customer_name,
c.customer_id,
r.order_id, 
r.order_date
FROM ranked r
JOIN Customers c
  ON r.customer_id = c.customer_id
WHERE r.rnk <= 3
ORDER BY c.name, c.customer_id, r.order_date DESC