-- script to create a trigger in MySQL to reset the valid_email column
-- only when the email has been changed
DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//

DELIMITER ;
