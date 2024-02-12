-- create an index on the name column of the users table

CREATE INDEX idx_name_first ON names (name(1));
