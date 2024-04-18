-- create3DatTable 실행후 코드 진행(mySQL샘플 사용 + on delete cascade)
use day3;
-- 생성 create
-- **************
-- begibber
-- **************
-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
insert into customers(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) values
(999,'JoonHo Seong','JoonHo','Seong','010xxxxxxxx','54, test_Adress',NULL,'Seoul',NULL,'44000','Korea',1370,'20000.00');

-- 2) **`products`** 테이블에 새 제품을 추가하세요.
insert into products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) values
('S10_1678_Test','1969 Harley Davidson Ultimate Chopper1','Motorcycles','1:10','Min Lin Diecast','This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.',7933,'48.81','95.70');


-- 진행을 위해 3번 4번 순서변경(외래키 참조를 위해 사무실 먼저 생성)
-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
insert into offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) values
('9999','San Francisco','+1 650 219 4782','100 Market Street','Suite 300','CA','USA','94080','NA');

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
insert into employees(employeeNumber,lastName,firstName,extension,email,officeCode,reportsTo,jobTitle) values
(9999,'JoonHo','Seong','x5800','joonho1366@gmail.com','9999',NULL,'President');

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
insert into orders(orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber) values
(99999,'2024-04-15','2024-04-17','2024-04-16','Shipped',NULL,999);

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
insert into orderdetails(orderNumber,productCode,quantityOrdered,priceEach,orderLineNumber) values
(99999,'S10_1678_Test',30,'136.00',10);

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
insert into payments(customerNumber,checkNumber,paymentDate,amount) values
(999,'JH999999','2034-10-19','6000.78');

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
insert into productlines(productLine,textDescription,htmlDescription,image) values
('Test','Trainning',NULL,NULL);
-- insert into products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) values
-- ('S10_1678_Test2','1969 Harley Davidson Ultimate Chopper1','Test','1:10','Min Lin Diecast','This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.',7933,'48.81','95.70');

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
insert into customers(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) values
(998,'JoonHo Seong','JoonHo','Seong','010xxxxxxxx','54, test_Adress2',NULL,'Tokyo',NULL,'44000','Japan',1370,'20000.00');

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
insert into products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) values
('S10_1949_Test','1952 Alpine Renault 13001','Classic Cars','1:10','Classic Metal Creations','Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.',7305,'98.58','214.30');

-- **************
-- middle class
-- **************
-- (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.

-- (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.

-- (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.

-- (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.

-- (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.

-- (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.

-- (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.

-- (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.

-- (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.

-- (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.


-- **************
-- advanced
-- **************
-- (1) **`customers`** 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.

-- (2) **`employees`** 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이트하세요.

-- (3) **`products`** 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.

-- (4) **`orders`** 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.

-- (5)**`orderdetails`** 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.


-- 읽기 read
-- **************
-- begibber
-- **************
-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select lastName, firstName, jobTitle from employees;

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
select addressLine1 from offices;

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders as o
order by o.orderDate desc
limit 10; 

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from orderdetails where orderNumber = 99999;

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerNumber=999;

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
select productLine, textDescription from productlines;

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where city = 'Seoul';

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where buyPrice > 90 and buyPrice <100;



-- **************
-- middle class
-- **************
-- (1) **`orders`** 테이블에서 특정 고객의 모든 주문을 조회하세요.

-- (2) **`orderdetails`** 테이블에서 특정 제품에 대한 모든 주문 상세 정보를 조회하세요.

-- (3) **`payments`** 테이블에서 특정 기간 동안의 모든 지불 정보를 조회하세요.

-- (4) **`employees`** 테이블에서 특정 직급의 모든 직원을 조회하세요.

-- (5) **`offices`** 테이블에서 특정 국가의 모든 사무실을 조회하세요.

-- (6) **`productlines`** 테이블에서 특정 제품 라인에 속하는 모든 제품을 조회하세요.

-- (7) **`customers`** 테이블에서 최근에 가입한 5명의 고객을 조회하세요.

-- (8) **`products`** 테이블에서 재고가 부족한 모든 제품을 조회하세요.

-- (9) **`orders`** 테이블에서 지난 달에 이루어진 모든 주문을 조회하세요.

-- (10) **`orderdetails`** 테이블에서 특정 주문에 대한 총 금액을 계산하세요.


-- **************
-- advanced
-- **************
-- (1) **`customers`** 테이블에서 각 지역별 고객 수를 계산하세요.

-- (2) **`products`** 테이블에서 각 제품 카테고리별 평균 가격을 계산하세요.

-- (3) **`employees`** 테이블에서 각 부서별 직원 수를 계산하세요.

-- (4) **`offices`** 테이블에서 각 사무실별 평균 직원 연봉을 계산하세요.

-- (5) **`orderdetails`** 테이블에서 가장 많이 팔린 제품 5개를 조회하세요.


-- 갱신 update
-- **************
-- begibber
-- **************

-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
update customers set addressLine2 = 'Test222' where customerNumber=999;

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
update products set buyPrice=40 where productCode ='S10_1678_Test';

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
update employees set jobTitle='VP Sales' where employeeNumber=9999;

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
set sql_safe_updates=0;
update offices set phone='123123123' where officeCode = 9999;
set sql_safe_updates=1;

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
update orders set status='Cancelled' where orderNumber=99999;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
update orderdetails set quantityOrdered=10 where orderNumber=99999;

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
update payments set amount = 3000 where customerNumber=999;

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update productlines set textDescription = 'TrainningTest' where productLine='Test';

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
-- 이메일 컬럼 추가
alter table customers add column email varchar(30) NULL;
-- 이메일 갱신
update customers set email = 'joonho1366@gmail.com' where customerNumber=999;

-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
update products set buyPrice = buyPrice * 0.9 where productLine ='Motorcycles';


-- **************
-- middle class
-- **************
-- (1) **`employees`** 테이블에서 여러 직원의 부서를 한 번에 갱신하세요.

-- (2) **`offices`** 테이블에서 여러 사무실의 위치를 한 번에 갱신하세요.

-- (3) **`orders`** 테이블에서 지난 달의 모든 주문의 배송 상태를 갱신하세요.

-- (4) **`orderdetails`** 테이블에서 여러 주문 상세의 가격을 한 번에 갱신하세요.

-- (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 갱신하세요.

-- (6) **`productlines`** 테이블에서 여러 제품 라인의 설명을 한 번에 갱신하세요.

-- (7) **`customers`** 테이블에서 특정 지역의 모든 고객의 연락처를 갱신하세요.

-- (8) **`products`** 테이블에서 특정 카테고리의 모든 제품 가격을 갱신하세요.

-- (9) **`employees`** 테이블에서 특정 직원의 모든 정보를 갱신하세요.

-- (10) **`offices`** 테이블에서 특정 사무실의 모든 정보를 갱신하세요.


-- **************
-- advanced
-- **************
-- (1) **`orders`** 테이블에서 지난 해의 모든 주문 상태를 갱신하세요.

-- (2) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 갱신하세요.

-- (3) **`payments`** 테이블에서 지난 달의 모든 지불 내역을 갱신하세요.

-- (4) **`productlines`** 테이블에서 모든 제품 라인의 정보를 갱신하세요.

-- (5) **`customers`** 테이블에서 모든 고객의 주소를 갱신하세요.


-- 삭제 delete
-- **************
-- begibber
-- **************
-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
delete from customers where customerNumber = 999; 

-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
delete from products where productCode ='S10_1678_Test';

-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
delete from employees where  employeeNumber=9999;

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
set sql_safe_updates = 0;
delete from offices where officeCode=9999;
set sql_safe_updates = 1;

-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
delete from orders where orderNumber=10100;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
delete from orderdetails where orderNumber=10105;

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
delete from payments where customerNumber=103;

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
delete from productlines where productLine = 'Test'; 

-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
delete from customers where city='Boston';

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
delete from products where productLine='Trains';


-- **************
-- middle class
-- **************
-- (1) **`employees`** 테이블에서 특정 부서의 모든 직원을 삭제하세요.

-- (2) **`offices`** 테이블에서 특정 국가의 모든 사무실을 삭제하세요.

-- (3) **`orders`** 테이블에서 지난 달의 모든 주문을 삭제하세요.

-- (4) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 삭제하세요.

-- (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 삭제하세요.

-- (6) **`productlines`** 테이블에서 여러 제품 라인을 한 번에 삭제하세요.

-- (7) **`customers`** 테이블에서 가장 오래된 5명의 고객을 삭제하세요.

-- (8) **`products`** 테이블에서 재고가 없는 모든 제품을 삭제하세요.

-- (9) **`employees`** 테이블에서 특정 직급의 모든 직원을 삭제하세요.

-- (10)**`offices`** 테이블에서 가장 작은 사무실을 삭제하세요.


-- **************
-- advanced
-- **************
-- (1) **`orders`** 테이블에서 지난 해의 모든 주문을 삭제하세요.

-- (2) **`orderdetails`** 테이블에서 가장 적게 팔린 제품의 모든 주문 상세를 삭제하세요.

-- (3) **`payments`** 테이블에서 특정 금액 이하의 모든 지불 내역을 삭제하세요.

-- (4) **`productlines`** 테이블에서 제품이 없는 모든 제품 라인을 삭제하세요.

-- (5) **`customers`** 테이블에서 최근 1년 동안 활동하지 않은 모든 고객을 삭제하세요.
