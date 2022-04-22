# Write your MySQL query statement below
# WITH A AS
#      (SELECT team_id, COUNT(*) AS team_size
#         FROM Employee
#        GROUP BY team_id)

# SELECT employee_id, A.team_size
#   FROM Employee as E
#        JOIN A ON E.team_id = A.team_id

SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size 
  FROM Employee