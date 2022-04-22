# Write your MySQL query statement below
WITH A AS
    (SELECT requester_id AS id1, accepter_id AS id2 
       FROM RequestAccepted
      UNION
     SELECT accepter_id AS id1, requester_id AS id2 
       FROM RequestAccepted)
SELECT id1 AS id, COUNT(id1) AS num
  FROM A
 GROUP BY id1
HAVING COUNT(id1) = (SELECT COUNT(id1)
                       FROM A
                      GROUP BY id1
                      ORDER BY COUNT(id1) DESC
                      LIMIT 1)
                      