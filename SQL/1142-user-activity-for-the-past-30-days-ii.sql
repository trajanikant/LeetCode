# Write your MySQL query statement below
SELECT IFNULL(ROUND (COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0) as average_sessions_per_user
  FROM Activity
 WHERE activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
# GROUP BY USER_ID