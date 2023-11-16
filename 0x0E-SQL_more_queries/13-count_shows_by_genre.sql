-- List all genres from the 'hbtn_0d_tvshows' database and display the number of shows linked to each.

-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>.
-- The first column must be called 'genre'.
-- The second column must be called 'number_of_shows'.
-- Don’t display a genre that doesn’t have any shows linked.
-- Results must be sorted in descending order by the number of shows linked.
-- Only one SELECT statement is allowed.

-- The database name will be provided as an argument to the mysql command.

SELECT genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
