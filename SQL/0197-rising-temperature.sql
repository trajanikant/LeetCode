# Write your MySQL query statement below
# SELECT A.ID
#   FROM WEATHER A 
#        JOIN WEATHER B ON A.ID = B.ID+1
#  WHERE A.TEMPERATURE > B.TEMPERATURE

SELECT A.ID
  FROM WEATHER A 
       JOIN WEATHER B ON DATEDIFF(A.RECORDDATE, B.RECORDDATE) = 1
 WHERE A.TEMPERATURE > B.TEMPERATURE