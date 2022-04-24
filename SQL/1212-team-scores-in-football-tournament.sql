# Write your MySQL query statement below
WITH A AS
     (SELECT host_team, host_goals, guest_goals FROM Matches
      UNION ALL
      SELECT guest_team, guest_goals, host_goals FROM Matches) 

SELECT team_id, team_name,
       SUM(CASE WHEN host_goals > guest_goals THEN 3
                WHEN host_goals = guest_goals THEN 1
                ELSE 0
           END) AS num_points
  FROM Teams AS T LEFT JOIN 
       A AS M ON T.team_id = M.host_team
 GROUP BY team_id
 ORDER BY num_points DESC, team_id ASC