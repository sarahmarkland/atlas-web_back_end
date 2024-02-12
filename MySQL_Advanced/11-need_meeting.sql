-- create a view named "need_meeting" that lists all students who have
-- a score under 80 and have not had a meeting in the last 30 days
DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 AND last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 30 DAY);
