# Write your MySQL query statement below
WITH total AS (
    SELECT COUNT(*) AS n_products
    FROM Product
)
SELECT c.customer_id
FROM Customer c
CROSS JOIN total t
GROUP BY c.customer_id, t.n_products
HAVING COUNT(DISTINCT c.product_key) = t.n_products;