-- Script that prepares a MySQL setup test for the project.
-- Create a database, new user, password with all privileges on the database for test.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
