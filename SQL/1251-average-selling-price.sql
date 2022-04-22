# Write your MySQL query statement below
SELECT P.product_id, ROUND(SUM(price * units) / SUM(units), 2) AS average_price
  FROM Prices AS P
       JOIN UnitsSold AS S ON P.product_id = S.product_id
                              AND S.purchase_date BETWEEN P.start_date AND P.end_date
 GROUP by P.product_id