# Write your MySQL query statement below
SELECT Q.id, Q.year, COALESCE(N.npv, 0) AS npv
  FROM Queries AS Q LEFT JOIN
       NPV AS N USING (id, year)
 ORDER BY Q.id, Q.year