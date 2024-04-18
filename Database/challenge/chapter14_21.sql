create database if not exists day3_challenge;

use day3_challenge;
-- 1
create table employees(
	id int auto_increment,
    name varchar(100),
    position varchar(100),
    salary decimal(10,2)
);
-- 2
insert into employees(name, position, salary) values
	('혜린','PM',90000),
	('은우','Frontend',80000),
    ('가을','Backend',92000),
    ('지수','Frontend',78000),
    ('민혁','Frontend',96000),
    ('하온','Backend',130000);
    
-- 3
select name, salary from employees;

-- 4
select name, salary from employees where position='Frontend' and salary <= 90000;

-- 5
set sql_safe_updates = 0;
update employees set salary = salary*1.1 where position='PM';
select position, salary from employees where position='PM';
set sql_safe_updates = 1;

-- 6 
set sql_safe_updates = 0;
update employees set salary = salary*1.05 where position='Backend';
set sql_safe_updates = 1;

-- 7
set sql_safe_updates = 0;
delete from employees where name='민혁';
set sql_safe_updates = 0;

-- 8
select position, avg(salary) as avg_salary from employees group by position;

drop table employees;