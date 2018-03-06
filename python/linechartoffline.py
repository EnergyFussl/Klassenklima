import pygal
from PIL import Image
import cairosvg
import shlex
import subprocess
import pymysql

import time 
from datetime import datetime, timedelta
from pygal.style import LightenStyle
arr=[0,1,2,3,4,5]

def drawChart():
<<<<<<< HEAD
    line_chart=pygal.Line(line_size=10)
    line_chart.title='Temperatur'
    line_chart.x_labels=map(lambda d: d.strftime('%H:%M'),[
        datetime(11,1,1,11,00),
	datetime(12,1,1,12,00),
	datetime(13,1,1,13,00),
	datetime(14,1,1,14,00),
	datetime(15,1,1,15,00),
	datetime(16,1,1,16,00)
=======
    line_chart=pygal.Line()
    line_chart.title='Temperatur'
    line_chart.x_labels=map(lambda d: d.strftime('%Y-%m-%d'),[
        datetime(2018,2,16),
        datetime(2018,2,17),
        datetime(2018,2,18),
        datetime(2018,2,19),
        datetime(2018,2,20),
        datetime(2018,2,21)
>>>>>>> 0e4ff0ae6ab5761850e49729fa7af5dfdd251f99
    ])
    line_chart.add("Temp",[arr[0],arr[1],arr[2],arr[3],arr[4],arr[5]])
    line_chart.render_to_png('/home/pi/Klassenklima/png/TempChart.png')

drawChart()
<<<<<<< HEAD








=======
>>>>>>> 0e4ff0ae6ab5761850e49729fa7af5dfdd251f99
