# Write your MySQL query statement below
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
  FROM (SELECT log_id, ROW_NUMBER() OVER (ORDER BY log_id) AS num
          FROM Logs) AS A
 GROUP BY log_id - num