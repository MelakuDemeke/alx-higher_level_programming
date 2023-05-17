-- Create the hbtn_0d_usa database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the states table if it doesn't already exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY unique_id (id)
);
