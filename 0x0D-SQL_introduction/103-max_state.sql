-- A script that lists the max of values by state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
