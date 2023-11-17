--  lists the number of records with the same score in the table second_table of the database
ALTER TABLE second_table
ADD COLUMN number INT;


UPDATE second_table
SET number = (SELECT COUNT(score) FROM second_table);