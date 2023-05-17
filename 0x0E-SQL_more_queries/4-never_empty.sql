-- Create the id_not_null table if it doesn't exist already
CREATE TABLE IF NOT EXISTS `id_not_null` (
  -- Define the id column as an integer with a default value of 1
  `id` INT DEFAULT 1,
  -- Define the name column as a string
  `name` VARCHAR(256)
);
