import pymysql

connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,autocommit=True)
cur = connection.cursor()
temp=22
hum=50
bar=1000
lux=300
co2=500
byt=100
str="INSERT INTO klima VALUES(null, "+str(temp)+", "+str(hum)+", "+str(bar)+", "+str(lux)+", "+str(co2)+", "+str(byt)+", "+"CURDATE()"+", "+"DATE_ADD(CURTIME(), INTERVAL 1 HOUR))"
print(str)
cur.execute(str)
print(cur.description)
print()
for row in cur:
    print(row)
cur.close()
connection.close()

