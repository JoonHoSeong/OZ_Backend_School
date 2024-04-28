use sakila;

select f.title from film as f
join film_actor as fa on f.film_id = fa.film_id
join actor as a on fa.actor_id = a.actor_id
where a.first_name = 'PENELOPE' and last_name = 'GUINESS';


select c.name, count(c.category_id) from category as c
join film_category as fc on c.category_id = fc.category_id
group by c.name;

select r.rental_date, f.title from rental as r
join customer as c on c.customer_id = r.customer_id
join inventory as i on i.inventory_id = r.inventory_id
join film as f on f.film_id = i.film_id
where r.customer_id =5;

select f.title, f.release_year from film as f
order by f.release_year desc limit 10;


select a.first_name , a.last_name from actor a
join film_actor as fa on fa.actor_id =  a.actor_id
join film as f on f.film_id = fa.film_id
where f.title = 'ACADEMY DINOSAUR';


select c.first_name , c.last_name from customer c
join rental as r on c.customer_id =  r.customer_id
join inventory as i on i.inventory_id = r.inventory_id
join film as f on f.film_id = i.film_id
where f.title = 'ACADEMY DINOSAUR';

select c.customer_id, c.first_name, c.last_name, max(r.rental_date), f.title from customer as c
join rental as r on c.customer_id = r.customer_id
join inventory as i on i.inventory_id = r.inventory_id
join film as f on f.film_id = i.film_id
group by c.customer_id, c.first_name, c.last_name, f.title;

select f.title, avg(DATEDIFF(r.return_date, r.rental_date)) from film as f
join inventory as i on i.film_id = f.film_id
join rental as r on i.inventory_id = r.inventory_id
group by f.title;

select f.title, count(r.rental_id)as num from film as f
join inventory as i on i.film_id = i.film_id
join rental as r on r.inventory_id = i.inventory_id
group by f.title
order by num desc limit 1;

select c.name, avg(f.rental_rate) from category as c
join film_category as fc on fc.category_id = c.category_id
join film as f on f.film_id = fc.film_id
group by c.name;

select year(payment_date), month(payment_date), sum(amount) from payment
group by year(payment_date), month(payment_date);

select a.first_name, a.last_name, count(fa.film_id) from actor as a
join film_actor as fa on a.actor_id = fa.actor_id
group by a.first_name, a.last_name;

select f.title, sum(p.amount) as total from film as f
join iventory as i on i.film_id = f.film_id
join rental as r on i.inventory_id = r.inventory_id
join payment as p on r.rental_id = p.rental_id
group by f.title
order by totla desc limit 1;

select f.title, f.rental_rate from film as f
where f.rental_rate > (select avg(rental_rate) from film);

select c.customer_id, c.first_name, c.last_name ,count(r.rental_id) as rent_num
from customer as c
join rental as r on c.customer_id = r.customer_id
group by c.customer_id
order by rent_num desc
limit 1;

select f.title, count(r.rental_id) as rental_num from film as f
join film_actor as fa on fa.film_id=f.film_id
join actor as a on a.actor_id = fa.actor_id
join inventory as i on i.film_id = f.film_id
join rental as r on r.inventory_id = i.inventory_id
where a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
group by f.title
order by rental_num desc
limit 1;

insert into film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
values ('New Adventure Movie', 'A thrilling adventure of the unknown', 2023, 1, 3, 4.99, 120, 19.99, 'PG', 'Trailers,Commentaries');

set sql_safe_updates = 0;
update customer set address_id = (select address_id from address where address = '47 MySakila Drive')
where customer_id = 5;
set sql_safe_updates = 1;

set sql_safe_updates = 0;
update rental
set return_date = NOW()
where rental_id = 200;
set sql_safe_updates = 1;

-- 외래키로 인해 불가능
delete from actor
where actor_id = 10;




