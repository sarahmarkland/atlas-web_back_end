-- write an SQL script that creates a table named users
-- The table should have the following columns:
-- id: an integer, never full, auto-incremented, and the primary key
-- email: a string, never null, max length of 255, unique
-- name: a string, max length of 255
-- country: enumeration of countries: US, CO, TN; never null (default
-- will be first element of the enumeration, US)

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)
