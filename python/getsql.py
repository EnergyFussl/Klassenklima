import pymysql
import datetime

def gettempsql():
   arr=[]
   returnarr=[]
   h=int('{:%H}'.format(datetime.datetime.now()))
#   h=5
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   i=0
   y='{:%Y}'.format(datetime.datetime.now())
   m='{:%m}'.format(datetime.datetime.now())
   d='{:%d}'.format(datetime.datetime.now())
#   y='2018'
 #  m='02'
  # d='13'

   while i<24:
      cmdstr="SELECT * FROM klima WHERE datum BETWEEN \""+y+"-"+m+"-"+d+" 00:00\" AND \""+y+"-"+m+"-"+d+" 23:59\" AND zeit BETWEEN \""+str(i)+":00\" AND \""+str(i)+":59\""
      cur.execute(cmdstr)
      result_set = cur.fetchall()
      j=0
      avg=0
      for row in result_set:
         j+=1
         avg+=row['temp']
      if j!=0:
         avg=avg/j
         avg=round(avg,2)
      arr.append(avg)
      i+=1

   if h >= 5:
      help=h-5
      while h>=help:
         returnarr.append(arr[h])
         h-=1
      return returnarr,(h+6)
   else:
      return [0,0,0,0,0,0],h

print(gettempsql())
