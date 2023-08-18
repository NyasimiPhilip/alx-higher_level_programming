-- Establish a database and define a table within it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Set up a table named 'cities'
CREATE TABLE IF NOT EXISTS cities (
id INT NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
state_id INT NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id)
);