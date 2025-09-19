# Write your MySQL query statement below
SELECT p.product_id, SUM(quantity) as total_quantity
FROM Sales AS s
INNER JOIN Product AS p
    ON s.product_id = p.product_id
GROUP BY product_id