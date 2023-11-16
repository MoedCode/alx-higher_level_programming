-- Create the table 'unique_id' on your MySQL server.

-- Description of 'unique_id':
--     - 'id' is an integer (INT) with the default value of 1 and must be unique.
--     - 'name' is a variable character (VARCHAR) with a length of 256 characters.

-- The database name will be provided as an argument to the mysql command.
-- If the table 'unique_id' already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);
