-- Select the name of the genre for the show Dexter
-- Join the tv_shows and tv_show_genres tables to get the genre for the show
-- Join the tv_genres table to get the name of the genre
-- Only show the genre name
-- Sort the results in ascending order by the genre name

SELECT g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`
       INNER JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;
