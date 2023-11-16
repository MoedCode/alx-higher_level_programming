-- Lists all shows without the genre Comedy in the 'hbtn_0d_tvshows' database.

-- The tv_genres table contains only one record where name = Comedy.
-- Each record should display: tv_shows.title.
-- Results must be sorted in ascending order by the show title.

SELECT s.`title`
FROM `tv_shows` AS s
WHERE s.`id` NOT IN (
    SELECT DISTINCT t.`show_id`
    FROM `tv_show_genres` AS t
    JOIN `tv_genres` AS g ON t.`genre_id` = g.`id`
    WHERE g.`name` = 'Comedy'
)
ORDER BY s.`title`;
