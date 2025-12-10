# Write your MySQL query statement below

WITH domains AS (
    SELECT
        SUBSTRING_INDEX(email, '@', -1) AS email_domain
    FROM Emails
)

SELECT
    email_domain,
    COUNT(*) AS count
FROM domains
WHERE email_domain LIKE '%.com'
GROUP BY email_domain
ORDER BY email_domain ASC
