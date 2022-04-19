# Write your MySQL query statement below
SELECT ROUND(SUM(percent) / COUNT(percent), 2) AS average_daily_percent
  FROM (SELECT A.action_date, COUNT(DISTINCT R.post_id) *100 / COUNT(DISTINCT A.post_id) as percent
          FROM Actions as A
               LEFT JOIN Removals as R ON A.post_id = R.post_id
         WHERE extra = 'spam'
         GROUP BY A.action_date) AS D