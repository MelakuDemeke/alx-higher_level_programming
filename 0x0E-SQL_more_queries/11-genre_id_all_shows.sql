-- Select the title of all TV shows in the database
-- Join it with the corresponding genre ID (if it exists) using a left join
-- Use IFNULL to display NULL if a TV show doesn't have a genre
-- Order the results in ascending order by the TV show title and genre ID

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;ORDER BY tv_shows.title ASC, genre_id;
