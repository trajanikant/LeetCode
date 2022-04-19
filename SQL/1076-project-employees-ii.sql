<!-- # Write your MySQL query statement below
SELECT P.project_id
  FROM Project as P
       JOIN Employee as E ON P.employee_id = E.employee_id
 GROUP BY P.project_id
 ORDER BY count(P.employee_id) DESC
 LIMIT 1 -->

SELECT project_id
  FROM Project
 GROUP BY project_id
HAVING COUNT(*) = (SELECT COUNT(*)
                     FROM Project
                    GROUP BY project_id
                    ORDER BY COUNT(*) DESC
                    LIMIT 1)