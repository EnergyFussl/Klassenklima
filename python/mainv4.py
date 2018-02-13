import pygal
from PIL import Image
import cairosvg
import shlex
import subprocess
import urllib.request
import urllib.parse
import pymysql
import time 

from pygal.style import LightenStyle


connection = pymysql.connect(host='localhost',user='sensoren',password='klassenklima',db='sensoren',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,autocommit=True)
cur = connection.cursor()

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
for line in fobj:
    if i>-1 and i<6:
       line.rstrip()
       waste,read[i]=line.split("=")
    if i>6 and i<19:
       line.rstrip()
       waste,help[i-7]=line.split("=")
       if i-7 == 0:
          tempfarbestart=strtointarr(help[i-7])
       if i-7 == 1:
          tempfarbeende=strtointarr(help[i-7])
       if i-7 == 2:    
          humfarbestart=strtointarr(help[i-7])
       if i-7 == 3:    
          humfarbeende=strtointarr(help[i-7])
       if i-7 == 4:    
          luxfarbestart=strtointarr(help[i-7])
       if i-7 == 5:    
          luxfarbeende=strtointarr(help[i-7])
       if i-7 == 6:    
          barfarbestart=strtointarr(help[i-7])
       if i-7 == 7:    
          barfarbeende=strtointarr(help[i-7])
       if i-7 == 10:    
          co2farbestart=strtointarr(help[i-7])
       if i-7 == 11:    
          co2farbeende=strtointarr(help[i-7])
    i+=1
fobj.close()

temp_max=int(read[0])
hum_max=int(read[3])
bar_max=int(read[2])
lux_max=int(read[1])
co2_max=int(read[4])

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


def gettemp():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x0027 -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")

                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x0024"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_temp_data=outputgatt.split(":")
                        raw_temp_bytes = raw_temp_data.split()
                        raw_ambient_temp = int( '0x'+ raw_temp_bytes[3]+ raw_temp_bytes[2], 16)
                        ambient_temp_int = raw_ambient_temp >> 2 & 0x3FFF
                        ambient_temp_celsius = float(ambient_temp_int) * 0.03125
                        if ambient_temp_celsius == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(ambient_temp_celsius)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-275


def gethum():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x002F -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x002C"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_hum_data=outputgatt.split(":")
                        raw_hum_bit = raw_hum_data.split()
                        raw_hum_data = int( '0x'+ raw_hum_bit[3]+ raw_hum_bit[2], 16)
                        raw_hum_data &= ~0x0003
                        hum = (float(raw_hum_data) / 65536)*100
                        if hum == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(hum)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1

def getbar():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x0037 -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x0034"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_bar_byte=outputgatt.split(":")
                        raw_bar_str = (raw_bar_byte.split())
                        raw_bar_data = int(('0x'+raw_bar_str[5])+(raw_bar_str[4])+raw_bar_str[3],16)
                        bar = raw_bar_data/100.0
                        if bar == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(bar)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1

def getlux():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x0047 -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x0044"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_lux_data=outputgatt.split(":")
                        raw_lux_list = raw_lux_data.split()
                        raw_lux_int=int('0x'+raw_lux_list[1]+raw_lux_list[0],16)
                        m = raw_lux_int & 0x0FFF
                        e = (raw_lux_int & 0xF000) >> 12;
                        if e==0:
                                e=1
                        else:
                                e=2<<(e-1)
                        lux=m * (0.01 * e)
                        if lux == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(lux)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1

def getco2():
  url = 'http://10.2.254.36'
  try:
    f = urllib.request.urlopen(url)
    arr=(f.read().decode('utf-8'))
    waste,arr=arr.split("<html>")
    print(arr)
    return arr
  except:
    print("error: no connecion to sensor")


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


def pushtosql():

   temp=gettemp()
   hum=gethum()
   bar=getbar()
   lux=getlux()
   co2=int(getco2())
   byt=-1
   if(temp>-275 and hum>-1 and bar>800 and lux>-1 and byt>-1 and co2>-1):
      arg="INSERT INTO klima VALUES(null, "+str(temp)+", "+str(hum)+", "+str(bar)+", "+str(lux)+", "+str(co2)+", "+str(byt)+", "+"CURDATE()"+", "+"DATE_ADD(CURTIME(), INTERVAL 1 HOUR))"
      print(arg)
      cur.execute(arg)
   else:
      print("invalide Value from Ti")
   time.sleep(10)

while 1:
    pushtosql()
    drawTemp()
    drawHumidity()
    drawBar()
    drawLux()
    drawCo2()
    crop("/home/pi/Klassenklima/png/TempHalfGauge")
    crop("/home/pi/Klassenklima/png/BarHalfGauge")
    crop("/home/pi/Klassenklima/png/HumHalfGauge")
    crop("/home/pi/Klassenklima/png/LuxHalfGauge")
    crop("/home/pi/Klassenklima/png/Co2HalfGauge")
    time.sleep(15)


cur.close()
connection.close()
