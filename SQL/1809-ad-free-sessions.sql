# Write your MySQL query statement below
SELECT session_id
  FROM Playback AS P LEFT JOIN
       Ads AS A ON P.customer_id = A.customer_id AND
                   (A.timestamp >= start_time AND A.timestamp <= end_time)
 WHERE timestamp IS NULL