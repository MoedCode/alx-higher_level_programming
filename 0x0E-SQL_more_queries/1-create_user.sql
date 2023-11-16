-- Create or ensure the existence of MySQL user 'user_0d_1' on the localhost server.
-- Grant all privileges to 'user_0d_1' with the password 'user_0d_1_pwd'.
-- If 'user_0d_1' already exists, the script will not fail.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
