-- Create the database 'hbtn_0d_usa' and the table 'states' in the database on your MySQL server.

-- Description of 'states':
--     - 'id' is an integer (INT) unique, auto-generated, cannot be null, and is a primary key.
--     - 'name' is a variable character (VARCHAR) with a length of 256 characters and cannot be null.

-- If the database 'hbtn_0d_usa' already exists, the script should not fail.
-- If the table 'states' already exists, the script should not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Inserting sample data
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
