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
    line_chart=pygal.Line()
    line_chart.title='Temperatur'
    line_chart.x_labels=map(lambda d: d.strftime('%Y-%m-%d'),[
        datetime(2018,2,16),
        datetime(2018,2,17),
        datetime(2018,2,18),
        datetime(2018,2,19),
        datetime(2018,2,20),
        datetime(2018,2,21)
    ])
    line_chart.add("Temp",[arr[0],arr[1],arr[2],arr[3],arr[4],arr[5]])
    line_chart.render_to_png('/home/pi/Klassenklima/png/TempChart.png')

drawChart()
