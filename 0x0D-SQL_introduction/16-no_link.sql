-- A script that lists all records
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
