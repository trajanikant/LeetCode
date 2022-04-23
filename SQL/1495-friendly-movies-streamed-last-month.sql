# Write your MySQL query statement below
SELECT DISTINCT title
  FROM Content AS C JOIN
       TVProgram AS TV ON C.content_id = TV.content_id
 WHERE Kids_content = 'Y' AND
       content_type = 'Movies' AND
       # MONTH(program_date) = 6 AND 
       # YEAR(program_date) = 2020 
       LEFT(program_date, 7) = "2020-06"
       