# Write your MySQL query statement below
# SELECT IFNULL((SELECT DISTINCT SALARY
#                  FROM EMPLOYEE
#                 ORDER BY SALARY DESC
#                 LIMIT 1 OFFSET 1), NULL)
#                 AS SECONDHIGHESTSALARY

SELECT
    (SELECT DISTINCT Salary
       FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 OFFSET 1) AS SecondHighestSalary