-- Write a SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order
DELIMITER //

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.amount
    WHERE name = NEW.item_id;
END;
//

DELIMITER ;
