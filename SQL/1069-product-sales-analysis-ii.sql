# Write your MySQL query statement below
SELECT product_id, SUM(quantity) AS total_quantity
  FROM Sales AS S JOIN
       Product AS P USING(product_id)
 GROUP BY product_id