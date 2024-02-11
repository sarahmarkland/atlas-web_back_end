-- Write a SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order
DELIMITER //

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_id INT;
    DECLARE order_quantity INT;

    SELECT NEW.item_id, NEW.quantity INTO item_id, order_quantity;

    UPDATE items
    SET quantity = quantity - order_quantity
    WHERE id = item_id;
END;
//

DELIMITER ;
