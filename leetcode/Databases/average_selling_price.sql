-- Method 1
WITH UnitsSoldPerProductDay AS (
    SELECT
        UnitsSoldPerProductDay.*
        , units_per_day * price AS total_price
    FROM (
        SELECT
            product_id
            , purchase_date
            , SUM(units) AS units_per_day
        FROM UnitsSold
        GROUP BY product_id, purchase_date
    ) UnitsSoldPerProductDay
    LEFT JOIN Prices
    USING(product_id)
    WHERE UnitsSoldPerProductDay.purchase_date BETWEEN Prices.start_date AND Prices.end_date
)

SELECT
    product_id
    , ROUND(SUM(total_price) / SUM(units_per_day), 2) AS average_price
FROM UnitsSoldPerProductDay
GROUP BY product_id;




-- Method 2:
SELECT
    product_id
    , ROUND(sum(units * price) / sum(units), 2) AS average_price
FROM (
    SELECT
        UnitsSold.product_id
        , units
        , price
    FROM UnitsSold
    LEFT JOIN Prices
    ON UnitsSold.product_id = Prices.product_id
    AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
) units_with_prices
GROUP BY product_id;
