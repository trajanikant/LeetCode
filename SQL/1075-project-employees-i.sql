# Write your MySQL query statement below
SELECT P.project_id, ROUND(AVG(E.experience_years), 2) as average_years
  FROM Project as P
       JOIN Employee as E ON P.employee_id = E.employee_id
 GROUP BY P.project_id
 