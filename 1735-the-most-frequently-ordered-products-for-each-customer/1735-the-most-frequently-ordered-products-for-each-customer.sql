# Write your MySQL query statement below

WITH counts AS (
    SELECT
    customer_id,
    product_id,
    COUNT(*) AS total
    FROM Orders
    GROUP BY customer_id, product_id
),
ranked AS (
    SELECT
    customer_id,
    product_id,
    DENSE_RANK() OVER (
        PARTITION BY customer_id
        ORDER BY total DESC
    ) AS rnk
    FROM counts
    GROUP BY customer_id, product_id
    ORDER BY customer_id
)

SELECT
r.customer_id,
r.product_id,
p.product_name
FROM ranked r
JOIN Products p
  ON r.product_id = p.product_id
WHERE rnk = 1


