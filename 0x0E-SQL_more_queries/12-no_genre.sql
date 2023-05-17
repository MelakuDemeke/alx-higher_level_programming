-- Select the title of all TV shows in the database
-- Join it with the corresponding genre ID (if it exists) using a left join
-- Only select records where the genre ID is NULL
-- Order the results in ascending order by the TV show title and genre ID
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
       WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;