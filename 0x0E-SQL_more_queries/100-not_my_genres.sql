-- Select the name of all genres not linked to the show "Dexter"
-- Use a NOT EXISTS subquery to exclude genres linked to "Dexter"
SELECT DISTINCT g.name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg ON g.id = sg.genre_id
INNER JOIN tv_shows AS s ON sg.show_id = s.id
WHERE NOT EXISTS (
  SELECT 1
  FROM tv_show_genres AS dsg
  INNER JOIN tv_shows AS ds ON dsg.show_id = ds.id
  WHERE dsg.genre_id = g.id AND ds.title = 'Dexter'
)
ORDER BY g.name;
