DROP DATABASE IF EXISTS fibonacci_db;
CREATE DATABASE fibonacci_db CHARACTER SET utf8 COLLATE utf8_general_ci;
DROP USER IF EXISTS 'fibonacci_db_user'@'%';
CREATE USER 'fibonacci_db_user'@'%' IDENTIFIED BY '12345678';
GRANT ALL PRIVILEGES ON fibonacci_db.* TO 'fibonacci_db_user'@'%';
USE fibonacci_db;

CREATE TABLE `fibonacci_metrics` (
  `request` text,
  `response` int
);
