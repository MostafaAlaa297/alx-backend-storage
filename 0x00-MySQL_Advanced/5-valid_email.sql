-- creates a trigger that resets the attribute valid_email only when the email has been changed
DELIMITER //

CREATE TRIGGER reset_valid_email_before_update
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
	SET valid_email = 0;
	END IF;
END//

DELIMITER;
