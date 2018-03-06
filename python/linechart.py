import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pymysql
import datetime

def getavgsql(wert):

   arr=[]
   returnarr=[]
   h=int('{:%H}'.format(datetime.datetime.now()))
   # h=4
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   i=0
   y='{:%Y}'.format(datetime.datetime.now())
   m='{:%m}'.format(datetime.datetime.now())
   d='{:%d}'.format(datetime.datetime.now())
  # y='2018'
 #  m='02'
#   d='27'

   while i<24:
      cmdstr="SELECT * FROM klima WHERE datum BETWEEN \""+y+"-"+m+"-"+d+" 00:00\" AND \""+y+"-"+m+"-"+d+" 23:59\" AND zeit BETWEEN \""+str(i)+":00\" AND \""+str(i)+":59\""
      cur.execute(cmdstr)
      result_set = cur.fetchall()
      j=0
      avg=0
      for row in result_set:
         j+=1
         avg+=row[wert]
      if j!=0:
         avg=avg/j
         avg=round(avg,1)
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






def drawChart(chname):
   namen=['Temperatur','Humidity','Lichtstärke','Luftdruck','CO2']
   py.sign_in('Klassenklima', 'EWRkIaqpdT5kStV3znTu')
   daten,uhr=getavgsql(chname)
   print(uhr)
   arr=[str(uhr-5)+":00",str(uhr-4)+":00",str(uhr-3)+":00",str(uhr-2)+":00",str(uhr-1)+":00",str(uhr)+":00"]
   print(daten)

   if chname=='temp':
      cname=namen[0]
      print(cname)

   elif chname=='hum':
      cname=namen[1]
   elif chname=='lux':
      cname=namen[2]
   elif chname=='bar':
      cname=namen[3]
   elif chname=='co2':
      cname=namen[4]

  # daten.insert(0,'0')	
   trace0 = go.Scatter(
      x=arr,
      y=daten,
      name=cname,
      line = dict(
         color=('rgb(255,0,0)'),
         width=6)
   )
   data=[trace0]
   layout=dict(
      title=cname,
      titlefont=dict(
         size=35,
         color='black'
      ),
      xaxis=dict(
         title='',
         titlefont=dict(
         family='Arial, sans-serif',
            size=30,
            color='black'
         ),
         showticklabels=True,
         #tickangle=45,
         tickfont=dict(
            family='Old Standard TT, serif',
            size=30,
            color='black'
         ),
      exponentformat='e',
      showexponent='All'
      ),
      yaxis=dict(
         title='',
         titlefont=dict(
            family='Arial, sans-serif',
            size=30,
            color='black'
         ),
         showticklabels=True,
            tickfont=dict(
            family='Old Standard TT, serif',
            size=30,
            color='black'
         ),
         exponentformat='e',
         showexponent='All'
     )
   )
   fig = dict(data=data,layout=layout)
   py.image.save_as(fig, filename='/home/pi/Klassenklima/png/'+chname+'Chart.png')



drawChart('temp')
drawChart("hum")
drawChart("bar")
drawChart("lux")
drawChart("co2")


