# Write your MySQL query statement below
SELECT ROUND(
        COUNT(DISTINCT CASE WHEN event_date = first_plus1 THEN player_id END) /
        COUNT(DISTINCT player_id),
        2
    ) AS fraction
FROM (
    SELECT player_id,
        event_date,
        MIN(event_date) OVER (PARTITION BY player_id) AS first_date,
        DATE_ADD(MIN(event_date) OVER (PARTITION BY player_id), INTERVAL 1 DAY) AS first_plus1
    FROM Activity
) AS t
WHERE event_date IN (first_date, first_plus1);