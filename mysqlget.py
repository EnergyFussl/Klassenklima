import pymysql

def gettempsql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (temp) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      return row['temp']

def gethumpsql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (hum) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      cur.close()
      connection.close()
      return row['hum']

def getbarsql():
   str="SELECT (bar) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      cur.close()
      connection.close()
      return row['bar']

def getluxsql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (lux) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set: 
      cur.close()
      connection.close()
      return row['lux']

def getco2sql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (co2) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      cur.close()
      connection.close()
      return row['co2']

def getbtysql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (bty) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      cur.close()
      connection.close()
      return row['bty']

print(getbtysql())


