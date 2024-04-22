use YES24;

select title, author from Books;

select * from Books where rating >= 8.0;

select * from Books where review >= 100;

select title, price from Books where price < 20000.0;

select * from Books where ranking_weeks >= 4;

select * from Books where author like '%신용하%';

select * from Books where publisher = '웅진지식하우스';

select author, count(*) from Books group by author;

select publisher, count(*) as Num from Books group by publisher order by Num desc limit 1;

select author,avg(rating) as avg_rating from Books group by author order by avg_rating desc limit 1;

select title, author from Books order by ranking limit 1;

select * from Books order by review desc ,sales desc limit 10;

select * from Books order by publishing desc limit 10;

select author, avg(rating) as author_rating from Books group by author;

select publishing, count(*) as book_num from Books group by publishing;

select title, avg(price) from Books group by title;

select * from Books order by review desc limit 5;

select ranking, avg(review) from Books group by ranking;

select * from Books where rating > (select avg(rating) from Books);

select title, price from Books where price > (select avg(price) from Books);

select title, review from Books where review > (select max(review) from Books);

select * from Books where sales < (select avg(sales) from Books);

select * from Books where author = (select author from Books group by author order by count(*) desc limit 1) order by publishing;

set sql_safe_updates = 0;
update Books set price=30000 where title = '던전밥 14';

update Books set title='Test' where author = '쿠이 료코 글그림/김민재 역';

delete from Books order by sales asc limit 1;

update Books set rating = rating+1 where publisher ='민음사';

select author, avg(rating), avg(sales) from Books group by author;

select publishing, avg(price) from Books group by publishing;

select publisher, count(*), avg(review) from Books group by publisher;

select ranking, avg(sales) from Books group by ranking;

select price, avg(review) from Books group by price;

select publisher, author , avg(sales) as avg_sales from Books group by publisher, author order by avg_sales desc;

select * from Books where review > (select avg(review) from Books) and price < (select avg(price) from Books);

select author, count(distinct title) as book_num from Books group by author order by book_num desc limit 1;

select author, title,max(price) from Books group by author, title;

select year(publishing) as YEAR, count(*), avg(price) from Books group by YEAR;

select publisher, max(rating) - min(rating) as diff from Books group by publisher order by diff desc limit 1;

select title, rating/sales as percent from Books where author = '신용하 저' order by percent desc limit 1;


