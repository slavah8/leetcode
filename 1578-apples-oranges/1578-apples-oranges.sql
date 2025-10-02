# Write your MySQL query statement below
SELECT
a.sale_date,
a.sold_num - o.sold_num AS diff
FROM Sales a
JOIN Sales o
  ON a.sale_date = o.sale_date
WHERE a.fruit = 'apples' AND o.fruit = 'oranges'
