# Write your MySQL query statement below
WITH A AS
     (SELECT country_name, AVG(weather_state) as weather_type
        FROM Weather AS W JOIN
             Countries as C ON W.country_id = C.country_id
       WHERE MONTH(day) = 11
       GROUP BY W.country_id
     )

SELECT country_name,
       CASE WHEN weather_type <= 15 THEN 'Cold'
            WHEN weather_type >= 25 THEN 'Hot'
            ELSE 'Warm'
       END AS weather_type
  FROM A