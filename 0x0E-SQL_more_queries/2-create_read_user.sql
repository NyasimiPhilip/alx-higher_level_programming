-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user and grant privileges
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

-- Set the default database for the user
USE hbtn_0d_2;

