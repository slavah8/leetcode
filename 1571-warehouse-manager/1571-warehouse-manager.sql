# Write your MySQL query statement below

WITH Volume AS (
    SELECT
        product_id,
        (Width * Length * Height) AS volume
    FROM Products

)

SELECT
    w.name AS warehouse_name,
    SUM((v.volume * w.units)) AS volume
FROM Volume v
JOIN Warehouse w
  ON v.product_id = w.product_id
GROUP BY w.name
