import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='sensoren',passwd='klassenklima',db='sensoren')

cur = conn.cursor()
cur.execute("CREATE TABLE klima (Id INT NOT NULL AUTO_INCREMENT,PRIMARY KEY (Id),temp float,hum float,bar float,lux float, co2 float, bty int, datum date, zeit time)")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()
