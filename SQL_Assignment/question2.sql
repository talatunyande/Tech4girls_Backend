/* using Tech4Girls_DB database */
USE Tech4Girls_DB;


/* creating table */ 
   CREATE TABLE IF NOT EXISTS Posts (
    id INT Primary Key AUTO_INCREMENT, 
    user_id   INT NOT NULL ,             -- user_id interger 
    title VARCHAR (255),                 -- tile to VARCHAR
    content VARCHAR(50),                    -- TEXT
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- default timestamp
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
-- inserting values to the table
INSERT INTO Posts (user_id,title,content)
VALUES 
(1,'FIRSTpost',"This is ama's first post"),
(2,'Abena goes to work','she expresses her experiance'),
(3,'Adjoa writes about her thoughts','That living in Ghana is not easy');

SELECT * FROM Posts;
