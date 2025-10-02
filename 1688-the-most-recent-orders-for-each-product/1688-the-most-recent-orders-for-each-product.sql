WITH max_day AS (
  SELECT product_id, MAX(order_date) AS max_date
  FROM Orders
  GROUP BY product_id
)
SELECT
  p.product_name,
  o.product_id,
  o.order_id,
  o.order_date
FROM max_day m
JOIN Orders o
  ON o.product_id = m.product_id
 AND o.order_date = m.max_date     -- keeps all ties on that day
JOIN Products p
  ON p.product_id = o.product_id
ORDER BY p.product_name, o.product_id, o.order_id;


