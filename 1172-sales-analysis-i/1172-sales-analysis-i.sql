# Write your MySQL query statement below

WITH prices AS (
    SELECT seller_id, SUM(price) AS total 
    FROM Sales
    GROUP BY seller_id
),
max_price AS (
    SELECT MAX(total) AS max_total
    FROM prices
)

SELECT p.seller_id
FROM prices p
JOIN max_price m
  ON p.total = m.max_total
