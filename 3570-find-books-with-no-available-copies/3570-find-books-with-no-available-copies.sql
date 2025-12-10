# Write your MySQL query statement below

WITH cte AS (
    SELECT
    book_id,
    COUNT(*) AS missing
FROM borrowing_records
WHERE return_date is NULL
GROUP BY book_id
)

SELECT
    l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    c.missing AS current_borrowers
FROM cte c
JOIN library_books l
  ON c.book_id = l.book_id
WHERE c.missing = l.total_copies
ORDER BY current_borrowers DESC, l.title ASC
