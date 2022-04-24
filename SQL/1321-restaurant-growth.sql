# Write your MySQL query statement below

with A as
     (SELECT visited_on, SUM(amount) AS amount 
        FROM Customer 
       GROUP BY 1)

SELECT DISTINCT C1.visited_on, SUM(C2.amount) AS amount, ROUND(SUM(C2.amount)/7,2) AS average_amount
  FROM A C1 INNER JOIN 
       A C2 ON (DATEDIFF(C1.visited_on, C2.visited_on)) BETWEEN 0 AND 6
 GROUP BY C1.visited_on
HAVING COUNT(C2.visited_on) > 6