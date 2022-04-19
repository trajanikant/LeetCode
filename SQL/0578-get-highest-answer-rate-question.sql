# Write your MySQL query statement below
SELECT question_id AS survey_log
  FROM Surveylog
 GROUP BY question_id
 ORDER BY SUM(IF(action='answer', 1, 0)) / SUM(IF(action<>'answer', 1, 0)) DESC, 
          question_id ASC
 LIMIT 1