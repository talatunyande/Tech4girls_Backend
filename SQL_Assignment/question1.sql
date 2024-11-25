/* Creating a database called Tech4Girls_DB */
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

SHOW DATABASES;

USE Tech4Girls_DB ;

/* creating a table called Users*/
CREATE TABLE IF NOT EXISTS Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100)  NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (username ,email)
VALUES
('ama','amaple@example.com'), -- username field
('Abens','abena@example.com'), -- email field
('adjoa','adjoa@example.com'); -- created_at field

SHOW TABLES;

SELECT * FROM Users;

