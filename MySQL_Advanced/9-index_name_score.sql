-- create an index named "idx_name_first_score" on the "score" column of the
-- name and the score
USE holberton;
CREATE INDEX idx_name_first_score ON names (name(1), score);
