# Write your MySQL query statement below
SELECT 
u.user_id AS buyer_id,
u.join_date, 
COUNT(CASE WHEN o.order_date BETWEEN '2019-01-01' AND '2019-12-31' THEN 1 END) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
  ON o.buyer_id = u.user_id 
GROUP BY u.user_id, u.join_date
 