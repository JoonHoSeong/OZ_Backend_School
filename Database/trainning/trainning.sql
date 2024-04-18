-- create database mydatabase;
-- show databases;
-- use mydatabase;
-- drop database if exists mydatabase;
-- use mysql;
-- select * from user;
-- create user 'trainning'@'localhost' identified by '1234';
-- select * from user;
-- set password for 'trainning'@'%' = 'trainning'
-- grant all privileges on *.* to 'trainning'@'localhost';
-- flush privileges;
-- show grants for 'trainning'@'localhost';
-- show grants
-- drop user 'trainning'@'%';
-- select * from user; 

-- create user 'test'@'localhost';
-- create database testdatabase;
-- use testdatabase;
-- create table users(
-- 	id int auto_increment primary key,
--     username varchar(50)  not null,
--     email varchar(100) unique,
--     is_business varchar(10) default False,
--     age int check (age>= 10)
-- );

-- drop table users;

-- CREATE TABLE users (
--     user_id INT PRIMARY KEY,
--     name VARCHAR(255),
--     age INT
-- );

-- INSERT INTO users (user_id, name, age)
-- VALUES (1, 'Alice', 25),
--        (2, 'Bob', 30),
--        (3, 'Charlie', 22),
--        (4, 'David', 33),
--        (5, 'Eve', 28);
--        
-- CREATE TABLE orders (
--     order_id INT PRIMARY KEY,
--     user_id INT,
--     order_date DATE
-- );

-- INSERT INTO orders (order_id, user_id, order_date)
-- VALUES (101, 1, '2023-01-01'),
--        (102, 2, '2023-02-01'),
--        (103, 1, '2023-02-15'),
--        (104, 3, '2023-03-01'),
--        (105, 4, '2023-03-10');


-- CREATE TABLE users (
--     user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
--     username TEXT NOT NULL,
--     email TEXT NOT NULL,
--     age INTEGER
-- );


-- INSERT INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25);
-- INSERT INTO users (username, email) VALUES ('jane_doe', 'jane@example.com');
-- INSERT INTO users (username, email, age) VALUES
--     ('alice', 'alice@example.com', 30),
--     ('bob', 'bob@example.com', 28),
--     ('charlie', 'charlie@example.com', 35);
-- INSERT INTO users (username, email) VALUES
--     ('david', 'david@example.com'),
--     ('elena', 'elena@example.com');
--     
-- INSERT IGNORE INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25);

-- INSERT INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25)
-- ON DUPLICATE KEY UPDATE age = 25;

-- INSERT INTO users (username, email) VALUES ('frank', 'frank@example.com');

-- INSERT INTO users (username, email, age)
-- VALUES ('john', 'john@example.com', 25),
--        ('jane', 'jane@example.com', 28),
--        ('bob', 'bob@example.com', 30);
--        
-- INSERT INTO users SET username='john', email='john@example.com', age=25;



-- CREATE TABLE users2 (
--     user_id INTEGER PRIMARY KEY,
--     username TEXT NOT NULL,
--     email TEXT NOT NULL,
--     age INTEGER
-- );


-- INSERT INTO users2 (user_id, username, email, age) VALUES (0,'john_doe', 'john@example.com', 25);
-- -- INSERT INTO users2 (username, email) VALUES ('jane_doe', 'jane@example.com');
-- INSERT INTO users2 (user_id,username, email, age) VALUES
--     (1,'alice', 'alice@example.com', 30),
--     (2,'bob', 'bob@example.com', 28),
--     (3,'charlie', 'charlie@example.com', 35);
-- INSERT INTO users2 (user_id,username, email) VALUES
--     (4,'david', 'david@example.com'),
--     (5,'elena', 'elena@example.com');
--     
-- INSERT IGNORE INTO users2 (user_id,username, email, age) VALUES (0,'john_doe', 'john@example.com', 25);

-- INSERT INTO users2 (user_id,username, email, age) VALUES (0,'john_doe', 'john@example.com', 25)
-- ON DUPLICATE KEY UPDATE age = 100;

-- INSERT INTO users2 (username, email) VALUES ('frank', 'frank@example.com');

-- INSERT INTO users2 (username, email, age)
-- VALUES ('john', 'john@example.com', 25),
--        ('jane', 'jane@example.com', 28),
--        ('bob', 'bob@example.com', 30);
--        
-- INSERT INTO users2 SET username='john', email='john@example.com', age=25;





