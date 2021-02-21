SELECT
    MIN(x - prev_x) AS shortest
FROM (
    SELECT
        x
        , LAG(x, 1) OVER (ORDER BY x) AS prev_x
    FROM point
) T;
