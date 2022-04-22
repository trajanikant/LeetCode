# Write your MySQL query statement below
WITH A AS
      (SELECT user1_id, user2_id
         FROM Friendship
        UNION
       SELECT user2_id, user1_id
         FROM Friendship)

SELECT DISTINCT page_id AS recommended_page
  FROM A
       JOIN Likes AS L ON A.user2_id = L.user_id
 WHERE A.user1_id = 1
       AND L.page_id NOT IN (SELECT page_id
                               FROM Likes
                              WHERE user_id = 1)
