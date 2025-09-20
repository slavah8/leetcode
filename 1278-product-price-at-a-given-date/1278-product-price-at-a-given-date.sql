# Write your MySQL query statement below
WITH latest AS (
    SELECT
    product_id,
    MAX(change_date) AS last_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
SELECT
p.product_id, COALESCE(pr.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS p
LEFT JOIN latest AS l
  ON p.product_id = l.product_id
LEFT JOIN Products AS pr 
  ON l.product_id = pr.product_id AND l.last_date = pr.change_date