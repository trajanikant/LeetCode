# Write your MySQL query statement below
SELECT NAME
  FROM CUSTOMER
 # WHERE REFEREE_ID <> 2
 #       OR REFEREE_ID IS NULL
 WHERE COALESCE (REFEREE_ID, 0) <> 2