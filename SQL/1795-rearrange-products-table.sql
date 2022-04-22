# Write your MySQL query statement below
WITH A AS
     (SELECT product_id, store1 AS price, 'store1' AS store
        FROM Products        
      UNION      
      SELECT product_id, store2 AS price, 'store2' AS store
        FROM Products
      UNION      
      SELECT product_id, store3 AS price, 'store3' AS store
        FROM Products)

SELECT product_id, store, price 
  FROM A
 WHERE price IS NOT NULL