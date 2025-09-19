# Write your MySQL query statement below
SELECT s.product_id, x.first_year, s.quantity, s.price
FROM Sales AS s
JOIN ( 
    SELECT product_id, MIN(year) AS first_year
    FROM Sales 
    GROUP BY product_id
) AS x
    ON s.product_id = x.product_id
    AND s.year = x.first_year;
