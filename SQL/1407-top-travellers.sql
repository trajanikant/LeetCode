# Write your MySQL query statement below
SELECT name, IFNULL(SUM(distance), 0) AS travelled_distance
  FROM Users AS U LEFT JOIN
       Rides AS R ON U.id = R.user_id
 GROUP BY user_id
 ORDER BY travelled_distance DESC,
          name ASC