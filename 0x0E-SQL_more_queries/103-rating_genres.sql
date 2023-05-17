-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg ON g.id = sg.genre_id
LEFT JOIN tv_show_ratings AS r ON sg.show_id = r.show_id
GROUP BY g.id
ORDER BY rating DESC;
