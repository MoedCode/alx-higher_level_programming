-- Lists all shows from the 'hbtn_0d_tvshows_rate' database by their rating.

-- Each record should display: tv_shows.title - rating sum.
-- Results must be sorted in descending order by the rating.

SELECT s.`title`, SUM(r.`rating`) AS `rating`
FROM `tv_shows` AS s
LEFT JOIN `tvshows_rate` AS r ON s.`id` = r.`show_id`
GROUP BY s.`id`, s.`title`
ORDER BY `rating` DESC;
