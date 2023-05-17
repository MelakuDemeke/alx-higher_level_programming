-- Create the force_name table if it doesn't exist already
CREATE TABLE IF NOT EXISTS `force_name` (
  -- Define the id column as an integer
  `id` INT,
  -- Define the name column as a non-null string
  `name` VARCHAR(256) NOT NULL,
  -- Define the id column as the primary key of the table
  PRIMARY KEY (`id`)
);
