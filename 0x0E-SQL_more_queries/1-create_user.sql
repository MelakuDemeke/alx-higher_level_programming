-- This script will create the MySQL user user_0d_1 with all privileges and a password of user_0d_1_pwd, if the user does not already exist.

-- Check if the user already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1');

-- If the user doesn't exist, create it and grant all privileges on all databases
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
