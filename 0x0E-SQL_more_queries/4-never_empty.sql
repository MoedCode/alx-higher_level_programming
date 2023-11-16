-- Create the table 'id_not_null' on your MySQL server.

-- Description of 'id_not_null':
--     - 'id' is an integer (INT) with the default value of 1.
--     - 'name' is a variable character (VARCHAR) with a length of 256 characters.

-- The database name will be provided as an argument to the mysql command.
-- If the table 'id_not_null' already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
