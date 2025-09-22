# Write your MySQL query statement below

WITH units AS (
SELECT p.product_name AS name, SUM(o.unit) AS total_units
FROM Products p
JOIN Orders o 
ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id
)
SELECT name AS product_name, total_units AS unit
FROM units
WHERE total_units >= 100
