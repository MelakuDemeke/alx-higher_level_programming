-- This script will list the privileges of MySQL users user_0d_1 and user_0d_2 on a server running on localhost

-- Select all rows from mysql.user where the user column is either 'user_0d_1' or 'user_0d_2'
SELECT * FROM mysql.user WHERE user = 'user_0d_1' OR user = 'user_0d_2';
