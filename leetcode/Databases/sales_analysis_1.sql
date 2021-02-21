# Write your MySQL query statement below
WITH sales_per_seller AS (
    SELECT
        seller_id
        , SUM(price) AS total_price
    FROM Sales
    GROUP BY seller_id
),
max_price AS(
    select MAX(total_price) AS max_total_price
    FROM sales_per_seller
)
SELECT
    seller_id
FROM sales_per_seller
WHERE total_price IN (select * from max_price);
