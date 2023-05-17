-- Select the titles of all shows and their genres (if any)
-- Use a LEFT JOIN to also include shows without a genre
-- Order the results in ascending order by the show title and genre name
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`
       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;