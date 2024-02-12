-- create an index on the name column of the users table

USE holberton;

-- drop the index if it exists
DROP INDEX IF EXISTS idx_name_first ON names;

-- create the index on first letter of name
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
