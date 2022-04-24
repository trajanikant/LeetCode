# Write your MySQL query statement below
SELECT name AS warehouse_name, SUM(Width * Length * Height * units) AS volume
  FROM Products AS P JOIN
       Warehouse AS W ON P.product_id = W.product_id
 GROUP BY warehouse_name