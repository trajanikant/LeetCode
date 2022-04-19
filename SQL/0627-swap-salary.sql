# Write your MySQL query statement below
UPDATE SALARY
   SET SEX = CASE 
                WHEN SEX = 'm' THEN 'f'
                ELSE 'm'
              END
             