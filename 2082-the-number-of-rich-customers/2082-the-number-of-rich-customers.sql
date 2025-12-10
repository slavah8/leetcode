# Write your MySQL query statement below

WITH maximums AS (
    SELECT
    customer_id,
    MAX(amount) AS maxx
FROM Store
GROUP BY customer_id
)
SELECT
    COUNT(*) AS rich_count
FROM maximums
WHERE maxx > 500