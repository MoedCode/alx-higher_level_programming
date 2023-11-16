-- Lists all genres not linked to the show Dexter from the 'hbtn_0d_tvshows' database.

-- The tv_shows table contains only one record where title = Dexter.
-- Each record should display: tv_genres.name.
-- Results must be sorted in ascending order by the genre name.

SELECT g.`name`
FROM `tv_genres` AS g
WHERE g.`id` NOT IN (
    SELECT DISTINCT t.`genre_id`
    FROM `tv_show_genres` AS t
    JOIN `tv_shows` AS s ON t.`show_id` = s.`id`
    WHERE s.`title` = 'Dexter'
)
ORDER BY g.`name`;
