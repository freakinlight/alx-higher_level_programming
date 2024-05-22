-- A script 
SELECT t.title, IFNULL(SUM(r.rate), 0) AS rating
FROM tv_shows AS t
LEFT JOIN tv_show_ratings AS r ON t.id = r.show_id
GROUP BY t.id
ORDER BY rating DESC;
