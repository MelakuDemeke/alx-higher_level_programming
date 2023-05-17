-- Create the unique_id table if it doesn't exist already
CREATE TABLE IF NOT EXISTS `unique_id` (
  -- Define the id column as an integer with a default value of 1 and must be unique
  `id` INT DEFAULT 1 UNIQUE,
  -- Define the name column as a string
  `name` VARCHAR(256)
);
