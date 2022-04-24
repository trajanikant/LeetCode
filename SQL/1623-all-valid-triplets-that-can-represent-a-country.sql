# Write your MySQL query statement below
SELECT SA.student_name AS member_A, 
       SB.student_name AS member_B, 
       SC.student_name AS member_C
  FROM SchoolA AS SA CROSS JOIN
       SchoolB AS SB CROSS JOIN
       SchoolC AS SC
 WHERE SA.student_id <> SB.student_id AND
       SB.student_id <> SC.student_id AND
       SC.student_id <> SA.student_id AND
       SA.student_name <> SB.student_name AND
       SB.student_name <> SC.student_name AND
       SC.student_name <> SA.student_name