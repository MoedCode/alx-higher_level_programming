-- Retrieve a list of all cities located in California from the 'hbtn_0d_usa' database.

-- The 'states' table contains only one record where the name is 'California'
-- (the id can vary, as illustrated in the example).

-- The results must be sorted in ascending order based on the 'id' column of the 'cities' table.
-- The use of the JOIN keyword is not allowed.

-- The database name will be provided as an argument to the mysql command.

SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN
    (SELECT `id`
	FROM `states`
	WHERE `name` = 'California')
ORDER BY `id`;
