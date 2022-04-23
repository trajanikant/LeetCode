# Write your MySQL query statement below
SELECT DISTINCT user_id, COUNT(*) AS followers_count
  FROM Followers
 GROUP BY user_id
 ORDER BY user_id