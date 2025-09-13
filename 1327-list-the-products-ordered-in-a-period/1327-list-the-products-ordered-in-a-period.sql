# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit  FROM Products AS P
INNER JOIN Orders AS O
ON O.product_id = P.product_id
WHERE order_date LIKE '2020-02-%'
GROUP BY O.product_id
HAVING SUM(unit) >= 100;
