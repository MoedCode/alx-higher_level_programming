-- Lists all genres in the 'hbtn_0d_tvshows_rate' database by their rating.

-- Each record should display: tv_genres.name - rating sum.
-- Results must be sorted in descending order by their rating.

SELECT g.`name`, SUM(r.`rating`) AS `rating`
FROM `tv_genres` AS g
JOIN `tv_show_genres` AS sg ON g.`id` = sg.`genre_id`
JOIN `tv_shows` AS s ON sg.`show_id` = s.`id`
LEFT JOIN `tvshows_rate` AS r ON s.`id` = r.`show_id`
GROUP BY g.`id`, g.`name`
ORDER BY `rating` DESC;
