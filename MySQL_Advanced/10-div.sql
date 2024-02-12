-- function that divides the first argument by the second argument
-- or returns 0 if the second argument is 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END //

DELIMITER ;
