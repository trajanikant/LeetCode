# Write your MySQL query statement below
WITH A AS
     (SELECT project_id, P.employee_id, experience_years, 
             MAX(experience_years) OVER (PARTITION BY project_id) AS max_years
        FROM Project AS P
             JOIN Employee AS E ON P.employee_id = E.employee_id)

SELECT project_id, employee_id
  FROM A
 WHERE A.experience_years = max_years