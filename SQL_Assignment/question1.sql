/* Creating a database called Tech4Girls_DB */
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
SHOW DATABASES;
USE Tech4Girls_DB ;

/* creating a table called Users*/
CREATE TABLE IF NOT EXISTS Users(

    id AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100)  NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
);
INSERT INTO Users (id ,username ,email,created_at)
VALUES
('ama','amaple@example.com','2024-11-01 10:30.00'), --username field
('Abens','abena@example.com','2024-11-02 12:00:00'), --email field
('adjoa','adjoa@example.com','2024-11-03 14:15:00'); -- created_at field
SHOW TABLES;

SELECT* FROM Users;

