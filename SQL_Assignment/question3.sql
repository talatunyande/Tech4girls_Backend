/* creating a courses table*/
USE Tech4Girls_DB;
CREATE TABLE IF NOT EXISTS Courses (
    id INT PRIMARY Key AUTO_INCREMENT,-- Primary key 
    course_name VARCHAR (100) NOT NULL,-- course datatype varchar
    description TEXT ,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);
-- creating another table called User_courses
CREATE TABLE User_Courses(
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id,course_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
    ); 
    -- Inserting Values in to courses
    INSERT INTO Courses(courses_name,description)
    VALUES 
    ('Data COmmunication','learning about networking'),
    ('Multimedia and webdesign','Learning webdesigning'),
    ('Mysql','Database');
-- User_courses
    INSERT INTO User_Courses
    (user_id,course_id)
    VALUES 
    (1,1),
    (1,2),
    (2,3);

    SHOW TABLES;
    SELECT *FROM Courses;


