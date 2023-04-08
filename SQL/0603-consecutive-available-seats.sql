-- # Write your MySQL query statement below

SELECT seat_id FROM Cinema
 WHERE free = 1 
       AND (seat_id+1 in (SELECT seat_id FROM Cinema WHERE free = 1) OR
            seat_id-1 in (SELECT seat_id FROM Cinema WHERE free = 1))
 ORDER by seat_id;

SELECT DISTINCT a.seat_id FROM Cinema
 