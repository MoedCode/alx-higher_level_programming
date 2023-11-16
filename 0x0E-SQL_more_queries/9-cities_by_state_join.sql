-- List all cities contained in the 'hbtn_0d_usa' database.

-- Each record should display: cities.id - cities.name - states.name.
-- Results must be sorted in ascending order by cities.id.
-- Only one SELECT statement is allowed.

-- The database name will be provided as an argument to the mysql command.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
