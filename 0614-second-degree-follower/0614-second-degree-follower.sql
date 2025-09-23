
WITH followers_count AS (
SELECT followee AS user, COUNT(*) AS followers
FROM Follow 
GROUP BY followee
),
following_count AS (
    SELECT follower AS user, COUNT(*) AS following
    FROM Follow
    GROUP BY follower
)

SELECT f1.user AS follower, f1.followers AS num
FROM followers_count f1
JOIN following_count f2
  ON f1.user = f2.user
ORDER BY f1.user ASC
