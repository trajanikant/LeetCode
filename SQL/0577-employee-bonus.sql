# Write your MySQL query statement below
SELECT name, bonus
  FROM Employee AS E LEFT JOIN
       Bonus AS B USING (empId)
 WHERE bonus < 1000 OR
       bonus IS NULL