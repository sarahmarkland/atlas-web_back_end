-- write am SQL script that creates a table named users in your database
-- The table should have the following columns:
-- id: an integer, never full, auto-incremented, and the primary key
-- email: a string, never null, max length of 255
-- password: a string, max length of 255

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
