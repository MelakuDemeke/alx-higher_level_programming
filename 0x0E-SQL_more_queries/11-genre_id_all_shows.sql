-- Select the title of all TV shows in the database
-- Join it with the corresponding genre ID (if it exists) using a left join
-- Use IFNULL to display NULL if a TV show doesn't have a genre
-- Order the results in ascending order by the TV show title and genre ID

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
