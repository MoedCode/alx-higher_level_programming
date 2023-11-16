-- List all genres of the show "Dexter" from the 'hbtn_0d_tvshows' database.

-- The 'tv_shows' table contains only one record where title = Dexter (but the id can be different).
-- Each record should display: tv_genres.name.
-- Results must be sorted in ascending order by the genre name.

SELECT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS t ON g.`id` = t.`genre_id`
INNER JOIN `tv_shows` AS s ON t.`show_id` = s.`id`
WHERE s.`title` = 'Dexter'
ORDER BY g.`name`;
