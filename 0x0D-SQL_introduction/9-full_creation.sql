-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert some rows
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8)
ON DUPLICATE KEY UPDATE
    id = VALUES(id),
    name = VALUES(name),
    score = VALUES(score);