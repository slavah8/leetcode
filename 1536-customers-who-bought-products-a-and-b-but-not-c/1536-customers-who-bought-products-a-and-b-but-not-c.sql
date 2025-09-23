# Write your MySQL query statement below

SELECT o.customer_id, c.customer_name
FROM Orders o
JOIN Customers c
ON o.customer_id = c.customer_id
GROUP BY o.customer_id, c.customer_name
HAVING COUNT(DISTINCT CASE WHEN o.product_name IN ('A', 'B') THEN o.product_name END) = 2
AND SUM(o.product_name = 'C') = 0
ORDER BY c.customer_id