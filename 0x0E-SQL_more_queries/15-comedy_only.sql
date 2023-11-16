-- Lists all Comedy shows in the 'hbtn_0d_tvshows' database.

-- The 'tv_genres' table contains only one record where name = Comedy (but the id can be different).
-- Each record should display: tv_shows.title.
-- Results must be sorted in ascending order by the show title.

SELECT s.`title`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS t ON g.`id` = t.`genre_id`
INNER JOIN `tv_shows` AS s ON t.`show_id` = s.`id`
WHERE g.`name` = 'Comedy'
ORDER BY s.`title`;
