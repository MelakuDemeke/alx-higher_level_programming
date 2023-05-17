-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.

SELECT DISTINCT t.title
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
  ON s.show_id = t.id
LEFT JOIN tv_genres AS g
  ON g.id = s.genre_id
WHERE t.title NOT IN (
  SELECT t2.title
  FROM tv_shows AS t2
  INNER JOIN tv_show_genres AS s2
    ON s2.show_id = t2.id
  INNER JOIN tv_genres AS g2
    ON g2.id = s2.genre_id
  WHERE g2.name = 'Comedy'
)
ORDER BY t.title ASC;
