import pygal
from PIL import Image
import cairosvg
import shlex
import subprocess
import pymysql

import time 
from pygal.style import LightenStyle

def strtointarr(arr):
        s=arr.split(",")
        a=[0,0,0]
        for i in range(0,3,1):
                a[i]=int(s[i])
        return a

fobj = open("config.txt", "r")
i=-1
help=[0,1,2,3,4,5,6,7,8,9,10,11]
read=[0,0,0,0,0,0]
farbe_def=[0,1,2,3,4,5,6,7,8,9,10,11]
for line in fobj:
   if i>-1 and i<6:
      line.rstrip()
      waste,read[i]=line.split("=")
   if i>6 and i<19:
      line.rstrip()
      waste,help[i-7]=line.split("=")
      farbe_def[i-7]=strtointarr(help[i-7])
      print(i)
      print(farbe_def[i-7])
   i+=1
fobj.close()


temp_max=int(read[0])
hum_max=int(read[3])
bat_max=int(read[5])
bar_max=int(read[2])
lux_max=int(read[1])
co2_max=int(read[4])


tempfarbestart=int(farbe_def[0])
tempfarbeende=farbe_def[1]
humfarbestart=farbe_def[2]
humfarbeende=farbe_def[3]
luxfarbestart=farbe_def[4]
luxfarbeende=farbe_def[5]
barfarbestart=farbe_def[6]
barfarbeende=farbe_def[7]
batfarbestart=farbe_def[8]
batfarbeende=farbe_def[9]
co2farbestart=farbe_def[10]
co2farbeende=farbe_def[11]

rot='#ff0000'
grun='#00ff00'
blau='#0000ff'
gelb='#ffff00'
orange='#ffa500'
schwarz='#000000'
weiß='#ffffff'


def crop(pfad):
  img = Image.open(pfad+".png")
  img.show()
  box = (150, 180, 670, 470)
  img_region = img.crop(box)
  img_region.save(pfad+"Crop.png")

def gettempsql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (temp) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
       temp=row['temp']
       return round(temp,1)
       
def gethumsql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (hum) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      cur.close()
      connection.close()
      hum=row['hum']
      return round(hum)

def getbarsql():
   connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
   cur = connection.cursor()
   str="SELECT (bar) FROM klima WHERE datum=curdate() ORDER BY Zeit DESC LIMIT 1"
   cur.execute(str)
   print(cur.description)
   result_set = cur.fetchall()
   for row in result_set:
      cur.close()
      connection.close()
      bar=row['bar']
      return round(bar)

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
      lux=row['lux']
      return round(lux)

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
      co2=row['co2']
      return  round(co2)

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
      

def drawTemp():
    x=gettempsql()
    tempfarbr=[0, 0, 0]
    x1=int((x/temp_max)*100)
    for i in range(0,3,1):
        tempfarbr[i]=int(tempfarbestart[i]+((tempfarbeende[i]-tempfarbestart[i])*(x1/100)))
        print(tempfarbr[i])
    
    
    c=tempfarbr[0]
    for i in range(1,3,1):
        c=c<<8
        c+=tempfarbr[i]
    
    print(c)
    hexstring=hex(c)
    print(hexstring)
    splitstring=hexstring.split("x")
    test=splitstring[1]
    print(test)
    farbe="#"+test
    dark_lighten_style = LightenStyle(farbe)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    grad_formatter = lambda x: '{:.10g}C'.format(x)
    gauge.value_formatter = grad_formatter
    gauge.add('', [{'value': x, 'max_value': temp_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/TempHalfGauge.png')
 

def drawHumidity():
    x=gethumsql()
    humfarbr=[0, 0, 0]
    x1=int((x/hum_max)*100)
    for i in range(0,3,1):
        humfarbr[i]=int(humfarbestart[i]+((humfarbeende[i]-humfarbestart[i])*(x1/100)))
        print(humfarbr[i])
    
    
    c=humfarbr[0]
    for i in range(1,3,1):
        c=c<<8
        c+=humfarbr[i]
    
    print(c)
    hexstring=hex(c)
    print(hexstring)
    splitstring=hexstring.split("x")
    test=splitstring[1]
    print(test)
    farbe="#"+test
    dark_lighten_style = LightenStyle(farbe)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': hum_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/HumHalfGauge.png')

def drawBar():
    x=getbarsql()
    barfarbr=[0, 0, 0]
    x1=int((x/bar_max)*100)
    for i in range(0,3,1):
        barfarbr[i]=int(barfarbestart[i]+(barfarbeende[i]-barfarbestart[i])*(x1/100))
        print(barfarbr[i])
    
    
    c=barfarbr[0]
    for i in range(1,3,1):
        c=c<<8
        c+=barfarbr[i]
    
    print(c)
    hexstring=hex(c)
    print(hexstring)
    splitstring=hexstring.split("x")
    test=splitstring[1]
    print(test)
    farbe="#"+test
    dark_lighten_style = LightenStyle(farbe)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} mBar'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': bar_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/BarHalfGauge.png')

def drawLux():
    x=getluxsql()
    luxfarbr=[0, 0, 0]
    x1=int((x/lux_max)*100)
    for i in range(0,3,1):
        luxfarbr[i]=int(luxfarbestart[i]+((luxfarbeende[i]-luxfarbestart[i])*(x1/100)))
        print(luxfarbr[i])
    
    
    c=luxfarbr[0]
    for i in range(1,3,1):
        c=c<<8
        c+=luxfarbr[i]
    
    print(c)
    hexstring=hex(c)
    print(hexstring)
    splitstring=hexstring.split("x")
    test=splitstring[1]
    print(test)
    farbe="#"+test
    dark_lighten_style = LightenStyle(farbe)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} lux'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('',[{'value': x, 'max_value': lux_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/LuxHalfGauge.png')

def drawBat():
    x=getbtysql()
    batfarbr=[0, 0, 0]
    x1=int((x/bat_max)*100)
    for i in range(0,3,1):
        batfarbr[i]=int(batfarbestart[i]+((batfarbeende[i]-batfarbestart[i])*(x1/100)))
        print(batfarbr[i])
    
    
    c=batfarbr[0]
    for i in range(1,3,1):
        c=c<<8
        c+=batfarbr[i]
    
    print(c)
    hexstring=hex(c)
    print(hexstring)
    splitstring=hexstring.split("x")
    test=splitstring[1]
    print(test)
    farbe="#"+test
    dark_lighten_style = LightenStyle(farbe)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} % Akku'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': bat_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/BatHalfGauge.png')

def drawCo2():
    x=getco2sql()
    co2farbr=[0, 0, 0]
    x1=int((x/co2_max)*100)
    for i in range(0,3,1):
        co2farbr[i]=int(co2farbestart[i]+((co2farbeende[i]-co2farbestart[i])*(x1/100)))
        print(co2farbr[i])
    
    
    c=co2farbr[0]
    for i in range(1,3,1):
        c=c<<8
        c+=co2farbr[i]
    
    print(c)
    hexstring=hex(c)
    print(hexstring)
    splitstring=hexstring.split("x")
    test=splitstring[1]
    print(test)
    farbe="#"+test
    dark_lighten_style = LightenStyle(farbe)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} ppm'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': bat_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/Co2HalfGauge.png')

while 1:
    drawTemp()
    drawHumidity()
    drawBar()
    drawLux()
    drawBat()
    drawCo2()
    crop("/home/pi/Klassenklima/png/TempHalfGauge")
    crop("/home/pi/Klassenklima/png/BarHalfGauge")
    crop("/home/pi/Klassenklima/png/HumHalfGauge")
    crop("/home/pi/Klassenklima/png/LuxHalfGauge")
    crop("/home/pi/Klassenklima/png/BatHalfGauge")
    crop("/home/pi/Klassenklima/png/Co2HalfGauge")
    time.sleep(15)
