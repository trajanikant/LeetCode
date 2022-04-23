# Write your MySQL query statement below
WITH A AS
     (SELECT 
      (SELECT COUNT(*)
         FROM NewYork
        WHERE score >= 90) AS NY,
      (SELECT COUNT(*)
        FROM California
       WHERE score >= 90) AS CAL
     )

SELECT CASE WHEN NY > CAL THEN 'New York University'
            WHEN CAL > NY THEN 'California University'
            ELSE 'No Winner'
       END AS 'winner'
  FROM A