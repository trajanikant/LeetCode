# Write your MySQL query statement below

SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
GROUP BY activity_date
