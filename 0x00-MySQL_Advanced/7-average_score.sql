-- Stored procedure computes and store the average score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE projects_count INT DEFAULT 0;

    -- Calculate the total score for the user
    SELECT IFNULL(SUM(score), 0) INTO total_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Calculate the number of projects for the user
    SELECT COUNT(*) INTO projects_count
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the user's average score
    UPDATE users
    SET users.average_score = IF(projects_count = 0, 0, total_score / projects_count)
    WHERE users.id = user_id;
END //
DELIMITER ;
