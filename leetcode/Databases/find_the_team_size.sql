# Write your MySQL query statement below

SELECT
    employee_id
    , team_sizes.team_size
FROM Employee
LEFT JOIN
    (
        SELECT
            team_id
            , count(*) AS team_size
        FROM Employee
        GROUP BY team_id
    ) team_sizes
USING (team_id);


SELECT
    employee_id
    , COUNT(*) OVER (PARTITION BY team_id) AS team_size
FROM Employee;
