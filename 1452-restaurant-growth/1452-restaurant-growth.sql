WITH daily AS (
  SELECT visited_on, SUM(amount) AS daily_amount
  FROM Customer
  GROUP BY visited_on
),
windowed AS (
  SELECT
    visited_on,
    SUM(daily_amount) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    AVG(daily_amount) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS avg_amount
  FROM daily
),
bounds AS (
  SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) AS start_day
  FROM daily
)
SELECT
  w.visited_on,
  w.amount,
  ROUND(w.avg_amount, 2) AS average_amount
FROM windowed w
JOIN bounds b
  ON w.visited_on >= b.start_day
ORDER BY w.visited_on;
