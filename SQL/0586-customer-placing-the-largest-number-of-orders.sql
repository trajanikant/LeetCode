# Write your MySQL query statement below
SELECT CUSTOMER_NUMBER
  FROM ORDERS
 GROUP BY CUSTOMER_NUMBER
HAVING COUNT(*) = (SELECT MAX(COUNTS)
                     FROM (SELECT COUNT(*) AS COUNTS
                             FROM ORDERS
                            GROUP BY CUSTOMER_NUMBER) AS A)
