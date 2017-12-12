import pygal
from PIL import Image
import cairosvg
import shlex
import subprocess
import pymysql

import time 
from pygal.style import LightenStyle

fobj = open("config.txt", "r")
i=-1
read=[0,0,0,0,0,0]
for line in fobj:
   if i>-1:
      line.rstrip()
      waste,read[i]=line.split("=")
   i+=1
fobj.close()


temp_max=int(read[0])
hum_max=int(read[3])
bat_max=int(read[5])
bar_max=int(read[2])
lux_max=int(read[1])
co2_max=int(read[4])
print(temp_max)



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
      

farbe='#000000'
grad=-1
farbe=['#0000ff', '#0000ff', '#0000ff', '#0000ff', '#0000ff', '#0000ff', '#0000ff',
     '#0001fe', '#0001fe', '#0001fe', '#0001fe', '#0001fe', '#0001fe', '#0001fe',
     '#0002fd', '#0002fd', '#0002fd', '#0002fd', '#0002fd', '#0002fd', '#0002fd',
     '#0003fc', '#0003fc', '#0003fc', '#0003fc', '#0003fc', '#0003fc', '#0003fc',
     '#0004fb', '#0004fb', '#0004fb', '#0004fb', '#0004fb', '#0004fb', '#0004fb',
     '#0005fa', '#0005fa', '#0005fa', '#0005fa', '#0005fa', '#0005fa', '#0005fa',
     '#0006f9', '#0006f9', '#0006f9', '#0006f9', '#0006f9', '#0006f9', '#0006f9',
     '#0007f8', '#0007f8', '#0007f8', '#0007f8', '#0007f8', '#0007f8', '#0007f8',
     '#0008f7', '#0008f7', '#0008f7', '#0008f7', '#0008f7', '#0008f7', '#0008f7',
     '#0009f6', '#0009f6', '#0009f6', '#0009f6', '#0009f6', '#0009f6', '#0009f6',
     '#000af5', '#000af5', '#000af5', '#000af5', '#000af5', '#000af5', '#000af5',
     '#000bf4', '#000bf4', '#000bf4', '#000bf4', '#000bf4', '#000bf4', '#000bf4',
     '#000cf3', '#000cf3', '#000cf3', '#000cf3', '#000cf3', '#000cf3', '#000cf3',
     '#000df2', '#000df2', '#000df2', '#000df2', '#000df2', '#000df2', '#000df2',
     '#000ef1', '#000ef1', '#000ef1', '#000ef1', '#000ef1', '#000ef1', '#000ef1',
     '#000ff0', '#000ff0', '#000ff0', '#000ff0', '#000ff0', '#000ff0', '#000ff0',
     '#001fe0', '#001fe0', '#001fe0', '#001fe0', '#001fe0', '#001fe0', '#001fe0',
     '#002fd0', '#002fd0', '#002fd0', '#002fd0', '#002fd0', '#002fd0', '#002fd0',
     '#003fc0', '#003fc0', '#003fc0', '#003fc0', '#003fc0', '#003fc0', '#003fc0',
     '#004fb0', '#004fb0', '#004fb0', '#004fb0', '#004fb0', '#004fb0', '#004fb0',
     '#005fa0', '#005fa0', '#005fa0', '#005fa0', '#005fa0', '#005fa0', '#005fa0',
     '#006f90', '#006f90', '#006f90', '#006f90', '#006f90', '#006f90', '#006f90',
     '#007f80', '#007f80', '#007f80', '#007f80', '#007f80', '#007f80', '#007f80',
     '#008f70', '#008f70', '#008f70', '#008f70', '#008f70', '#008f70', '#008f70',
     '#009f60', '#009f60', '#009f60', '#009f60', '#009f60', '#009f60', '#009f60',
     '#00af50', '#00af50', '#00af50', '#00af50', '#00af50', '#00af50', '#00af50',
     '#00bf40', '#00bf40', '#00bf40', '#00bf40', '#00bf40', '#00bf40', '#00bf40',
     '#00cf30', '#00cf30', '#00cf30', '#00cf30', '#00cf30', '#00cf30', '#00cf30',
     '#00df20', '#00df20', '#00df20', '#00df20', '#00df20', '#00df20', '#00df20',
     '#00ef10', '#00ef10', '#00ef10', '#00ef10', '#00ef10', '#00ef10', '#00ef10',
     '#00ff00', '#00ff00', '#00ff00', '#00ff00', '#00ff00', '#00ff00', '#00ff00',
     '#01fe00', '#01fe00', '#01fe00', '#01fe00', '#01fe00', '#01fe00', '#01fe00',
     '#02fd00', '#02fd00', '#02fd00', '#02fd00', '#02fd00', '#02fd00', '#02fd00',
     '#03fc00', '#03fc00', '#03fc00', '#03fc00', '#03fc00', '#03fc00', '#03fc00',
     '#04fb00', '#04fb00', '#04fb00', '#04fb00', '#04fb00', '#04fb00', '#04fb00',
     '#05fa00', '#05fa00', '#05fa00', '#05fa00', '#05fa00', '#05fa00', '#05fa00',
     '#06f900', '#06f900', '#06f900', '#06f900', '#06f900', '#06f900', '#06f900',
     '#07f800', '#07f800', '#07f800', '#07f800', '#07f800', '#07f800', '#07f800',
     '#08f700', '#08f700', '#08f700', '#08f700', '#08f700', '#08f700', '#08f700',
     '#09f600', '#09f600', '#09f600', '#09f600', '#09f600', '#09f600', '#09f600',
     '#0af500', '#0af500', '#0af500', '#0af500', '#0af500', '#0af500', '#0af500',
     '#0bf400', '#0bf400', '#0bf400', '#0bf400', '#0bf400', '#0bf400', '#0bf400',
     '#0cf300', '#0cf300', '#0cf300', '#0cf300', '#0cf300', '#0cf300', '#0cf300',
     '#0df200', '#0df200', '#0df200', '#0df200', '#0df200', '#0df200', '#0df200',
     '#0ef100', '#0ef100', '#0ef100', '#0ef100', '#0ef100', '#0ef100', '#0ef100',
     '#0ff000', '#0ff000', '#0ff000', '#0ff000', '#0ff000', '#0ff000', '#0ff000',
     '#1fe000', '#1fe000', '#1fe000', '#1fe000', '#1fe000', '#1fe000', '#1fe000',
     '#2fd000', '#2fd000', '#2fd000', '#2fd000', '#2fd000', '#2fd000', '#2fd000',
     '#3fc000', '#3fc000', '#3fc000', '#3fc000', '#3fc000', '#3fc000', '#3fc000',
     '#4fb000', '#4fb000', '#4fb000', '#4fb000', '#4fb000', '#4fb000', '#4fb000',
     '#5fa000', '#5fa000', '#5fa000', '#5fa000', '#5fa000', '#5fa000', '#5fa000',
     '#6f9000', '#6f9000', '#6f9000', '#6f9000', '#6f9000', '#6f9000', '#6f9000',
     '#7f8000', '#7f8000', '#7f8000', '#7f8000', '#7f8000', '#7f8000', '#7f8000',
     '#8f7000', '#8f7000', '#8f7000', '#8f7000', '#8f7000', '#8f7000', '#8f7000',
     '#9f6000', '#9f6000', '#9f6000', '#9f6000', '#9f6000', '#9f6000', '#9f6000',
     '#af5000', '#af5000', '#af5000', '#af5000', '#af5000', '#af5000', '#af5000',
     '#bf4000', '#bf4000', '#bf4000', '#bf4000', '#bf4000', '#bf4000', '#bf4000',
     '#cf3000', '#cf3000', '#cf3000', '#cf3000', '#cf3000', '#cf3000', '#cf3000',
     '#df2000', '#df2000', '#df2000', '#df2000', '#df2000', '#df2000', '#df2000',
     '#ef1000', '#ef1000', '#ef1000', '#ef1000', '#ef1000', '#ef1000', '#ef1000',
     '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
     ]

grad=-1
farbehum=['#0000ff', '#0000ff',
          '#0001fe', '#0001fe',
          '#0002fd',
          '#0003fc', '#0003fc',
          '#0004fb', '#0004fb',
          '#0005fa',
          '#0006f9', '#0006f9',
          '#0007f8', '#0007f8',
          '#0008f7',
          '#0009f6', '#0009f6',
          '#000af5', '#000af5',
          '#000bf4',
          '#000cf3', '#000cf3',
          '#000df2', '#000df2',
          '#000ef1',
          '#000ff0', '#000ff0',
          '#001fe0', '#001fe0',
          '#002fd0',
          '#003fc0', '#003fc0',
          '#004fb0', '#004fb0',
          '#005fa0',
          '#006f90', '#006f90',
          '#007f80', '#007f80',
          '#008f70',
          '#009f60', '#009f60',
          '#00af50', '#00af50',
          '#00bf40',
          '#00cf30', '#00cf30',
          '#00df20', '#00df20',
          '#00ef10',
          '#00ff00', '#00ff00',
          '#01fe00', '#01fe00',
          '#02fd00',
          '#03fc00', '#03fc00',
          '#04fb00', '#04fb00',
          '#05fa00',
          '#06f900', '#06f900',
          '#07f800', '#07f800',
          '#08f700',
          '#09f600', '#09f600',
          '#0af500', '#0af500',
          '#0bf400',
          '#0cf300', '#0cf300',
          '#0df200', '#0df200',
          '#0ef100',
          '#0ff000', '#0ff000',
          '#1fe000', '#1fe000',
          '#2fd000',
          '#3fc000', '#3fc000',
          '#4fb000', '#4fb000',
          '#5fa000',
          '#6f9000', '#6f9000',
          '#7f8000', '#7f8000',
          '#8f7000',
          '#9f6000', '#9f6000',
          '#af5000', '#af5000',
          '#bf4000',
          '#cf3000', '#cf3000',
          '#df2000', '#df2000',
          '#ef1000',
          '#ff0000', '#ff0000',
          ]

farbebat=['#00ff00', '#00ff00',
          '#01ff00', '#01ff00',
          '#02ff00',
          '#03ff00', '#03ff00',
          '#04ff00', '#04ff00',
          '#05ff00',
          '#06ff00', '#06ff00',
          '#07ff00', '#07ff00',
          '#08ff00',
          '#09ff00', '#09ff00',
          '#0aff00', '#0aff00',
          '#0bff00',
          '#0cff00', '#0cff00',
          '#0dff00', '#0dff00',
          '#0eff00',
          '#0fff00', '#0fff00',
          '#1fff00', '#1fff00',
          '#2fff00',
          '#3fff00', '#3fff00',
          '#4fff00', '#4fff00',
          '#5fff00',
          '#6fff00', '#6fff00',
          '#7fff00', '#7fff00',
          '#8fff00',
          '#9fff00', '#9fff00',
          '#afff00', '#afff00',
          '#bfff00',
          '#cfff00', '#cfff00',
          '#dfff00', '#dfff00',
          '#efff00',
          '#ffff00', '#ffff00',
          '#fffe00', '#fffe00',
          '#fffd00',
          '#fffc00', '#fffc00',
          '#fffb00', '#fffb00',
          '#fffa00',
          '#fff900', '#fff900',
          '#fff800', '#fff800',
          '#fff700',
          '#fff600', '#fff600',
          '#fff500', '#fff500',
          '#fff400',
          '#fff300', '#fff300',
          '#fff200', '#fff200',
          '#fff100',
          '#fff000', '#fff000',
          '#ffe000', '#ffe000',
          '#ffd000',
          '#ffc000', '#ffc000',
          '#ffb000', '#ffb000',
          '#ffa000',
          '#ff9000', '#ff9000',
          '#ff8000', '#ff8000',
          '#ff7000',
          '#ff6000', '#ff6000',
          '#ff5000', '#ff5000',
          '#ff4000',
          '#ff3000', '#ff3000',
          '#ff2000', '#ff2000',
          '#ff1000',
          '#ff0000', '#ff0000',
          ]

def drawTemp():
    x=gettempsql()
    tempfarb='#000000'
    x1=(temp_max*10)+1
    for i in range(0, x1, 1):
        if(i == (x*10)):
            tempfarb=farbe[i]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    grad_formatter = lambda x: '{:.10g}C'.format(x)
    gauge.value_formatter = grad_formatter
    gauge.add('', [{'value': x, 'max_value': temp_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/TempHalfGauge.png')
 

def drawHumidity():
    x=gethumsql()
    tempfarb='#000000'
    tempfarb=farbehum[x]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': hum_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/HumHalfGauge.png')

def drawBar():
    x=getbarsql()
    tempfarb='#000000'
    x1=bar_max/100
    x1=int(x1)
    z=-1

    for j in range(0, bar_max, 1):
        z=z+1
        for i in range(j*x1, (j+1)*x1, 1):
            if(i == x):
                tempfarb=farbehum[z]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} mBar'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': bar_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/BarHalfGauge.png')

def drawLux():
    x=getluxsql()
    tempfarb='#000000'
    x1=lux_max/100
    x1=int(x1)
    z=-1

    for j in range(0, lux_max, 1):
        z=z+1
        for i in range(j*x1, (j+1)*x1, 1):
            if(i == x):
                tempfarb=farbehum[z]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} lux'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('',[{'value': x, 'max_value': lux_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/LuxHalfGauge.png')

def drawBat():
    x=getbtysql()
    wert=100-x
    tempfarb='#000000'
    tempfarb=farbebat[wert]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.40, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} % Akku'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('', [{'value': x, 'max_value': bat_max}])
    gauge.render_to_png('/home/pi/Klassenklima/png/BatHalfGauge.png')
    
while 1:
    drawTemp()
    drawHumidity()
    drawBar()
    drawLux()
    drawBat()
    crop("/home/pi/Klassenklima/png/TempHalfGauge")
    crop("/home/pi/Klassenklima/png/BarHalfGauge")
    crop("/home/pi/Klassenklima/png/HumHalfGauge")
    crop("/home/pi/Klassenklima/png/LuxHalfGauge")
    crop("/home/pi/Klassenklima/png/BatHalfGauge")
    time.sleep(15)
