# Write your MySQL query statement below


SELECT DISTINCT s1.buyer_id
FROM Sales s1
JOIN Product p1
  ON s1.product_id = p1.product_id
WHERE p1.product_name = 'S8' AND NOT EXISTS (
    SELECT 1
    FROM Sales s2
    JOIN Product p2
      ON s2.product_id = p2.product_id
    WHERE s2.buyer_id = s1.buyer_id AND p2.product_name = 'iPhone'
)

