-- Create the database 'hbtn_0d_usa' and the table 'cities' within it on your MySQL server.

-- Description of 'cities':
--     - 'id' is an integer (INT) that is unique, auto-generated, cannot be null, and serves as the primary key.
--     - 'state_id' is an integer (INT) that cannot be null and must be a FOREIGN KEY, referencing the 'id' column of the 'states' table.
--     - 'name' is a variable character (VARCHAR) with a length of 256 characters and cannot be null.

-- If the database 'hbtn_0d_usa' already exists, the script should not fail.
-- If the table 'cities' already exists within the database, the script should not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
);

-- Inserting sample data
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");
