-- # Write your MySQL query statement below

-- SELECT
-- ROUND( IFNULL(
--     (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS A) /
--     (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS B)
--           , 0)
--   , 2) AS accept_rate;

# Write your MySQL query statement below

SELECT IFNULL(ROUND(COUNT(DISTINCT requester_id, accepter_id) / 
             COUNT(DISTINCT sender_id, send_to_id), 2), 0) AS accept_rate
  FROM FriendRequest, RequestAccepted