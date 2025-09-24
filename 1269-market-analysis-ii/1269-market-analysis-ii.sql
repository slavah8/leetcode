# Write your MySQL query statement below

WITH sales AS (
    SELECT
    o.seller_id, o.order_date, i.item_brand, ROW_NUMBER() OVER (
        PARTITION BY seller_id
        ORDER BY order_date
    ) AS rn
    FROM Orders o
    JOIN Items i
      ON o.item_id = i.item_id
),
second_sale AS (
    SELECT seller_id, item_brand AS second_brand
    FROM sales
    WHERE rn = 2
)

SELECT
u.user_id AS seller_id,
CASE
  WHEN s.second_brand IS NULL THEN 'no'
  WHEN s.second_brand = u.favorite_brand THEN 'yes'
  ELSE 'no'
  END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN second_sale s
  ON u.user_id = s.seller_id
