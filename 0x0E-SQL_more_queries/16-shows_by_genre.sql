-- Lists all shows and all genres linked to each show from the 'hbtn_0d_tvshows' database.

-- If a show doesn’t have a genre, display NULL in the genre column.
-- Each record should display: tv_shows.title - tv_genres.name.
-- Results must be sorted in ascending order by the show title and genre name.

SELECT s.`title`, g.`name`
FROM `tv_shows` AS s
LEFT JOIN `tv_show_genres` AS t ON s.`id` = t.`show_id`
LEFT JOIN `tv_genres` AS g ON t.`genre_id` = g.`id`
ORDER BY s.`title`, g.`name`;
