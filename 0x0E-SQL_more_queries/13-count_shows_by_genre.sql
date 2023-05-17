-- Select the genre and count the number of TV shows with that genre
-- Join the tv_shows and tv_show_genres tables to get the genre for each TV show
-- Only count shows that have a genre linked (i.e. where genre_id is not NULL)
-- Group the results by genre
-- Only show genres that have at least one linked TV show
-- Order the results in descending order by the number of shows linked
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
 