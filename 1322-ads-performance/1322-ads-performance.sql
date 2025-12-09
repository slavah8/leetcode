# Write your MySQL query statement below

WITH stats AS (
    SELECT
        ad_id,
        SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) AS clicks,
        SUM(CASE WHEN action = 'Viewed' THEN 1 ELSE 0 END) AS views
        FROM Ads
        GROUP BY ad_id
)

SELECT
    ad_id,
    ROUND(
        CASE
            WHEN clicks + views = 0 THEN 0
            ELSE (clicks / (clicks + views)) * 100.0
        END, 
        2
    ) AS ctr
FROM stats
ORDER BY ctr DESC, ad_id ASC;
