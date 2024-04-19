import pymysql

conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='root',  # 데이터베이스 비밀번호
    db='fake_airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def sql_execute(sql) :
    with conn.cursor() as cursor :
        sql = sql
        cursor.execute(sql)
        if 'select' in sql.lower() :
            return cursor.fetchall()
        conn.commit()

# Practice
## 1
sql = f"insert into Products(productName, price, stockQuantity) values ('Python Book', 29.99, 99)"
sql_execute(sql)

## 2
sql = 'select * from Customers'
result = sql_execute(sql)
for i in result :
    print(i)
    
## 3
ordernum = 10
productName = 'Python Book'
sql = f"update Products set stockQuantity = stockQuantity-{ordernum} where productName='{productName}'"
sql_execute(sql)

## 4
sql = "select customerID, sum(totalAmount) as PayPrice from Orders group by customerID"
result = sql_execute(sql)
for i in result :
    print(i)
    
## 5
newEmail = 'test@test.com'
customerID = 5
sql = f"update Customers set email = '{newEmail}' where customerID={customerID}"
sql_execute(sql)

## 6
orderId = 15
sql = f'delete from Orders where orderID={orderId}'
sql_execute(sql)

## 7
productName = 'Python Book'
sql = f"select * from Products where productName='{productName}'"
result = sql_execute(sql)
for i in result :
    print(i)
    
## 8 
customerID=3
sql = f"select * from orders where customerID={customerID}"
result = sql_execute(sql)
for i in result :
    print(i)
    
## 9
sql = 'select customerID, count(*) as OrderNum from Orders group by customerID limit 1'
result = sql_execute(sql)
print(result[0])



conn.close()


