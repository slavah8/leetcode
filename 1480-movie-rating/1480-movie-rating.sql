# Write your MySQL query statement below
WITH user_counts AS (
SELECT u.name, COUNT(*) AS ratings_count
FROM MovieRating m
JOIN Users u
ON m.user_id = u.user_id
GROUP BY m.user_id, u.name
),
top_user AS (
    SELECT name 
    FROM user_counts
    ORDER BY ratings_count DESC, name ASC
    LIMIT 1
),
feb_ratings AS (
    SELECT m.title, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m
    ON mr.movie_id = m.movie_id
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id, m.title
),
top_movie AS (
    SELECT title
    FROM feb_ratings
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
)

SELECT name AS results FROM top_user
UNION ALL
SELECT title FROM top_movie