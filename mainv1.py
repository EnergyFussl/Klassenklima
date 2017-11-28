import pygal
import shlex
import subprocess
from pygal.style import LightenStyle

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
    x=34
    tempfarb='#000000'

    for i in range(0, 421, 1):
        if(i == (x*10)):
            tempfarb=farbe[i]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=dark_lighten_style)
    grad_formatter = lambda x: '{:.10g}C'.format(x)
    gauge.value_formatter = grad_formatter
    gauge.add('Temperatur', [{'value': x, 'max_value': 42}])
    gauge.render_to_file('TempHalfGauge.svg')

def drawHumidity():
    x=50
    tempfarb='#000000'

    for i in range(0, 101, 1):
        if(i == x):
            tempfarb=farbehum[i]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('Luftfeuchtigkiet', [{'value': x, 'max_value': 100}])
    gauge.render_to_file('HumHalfGauge.svg')

def drawBar():
    x=1490
    tempfarb='#000000'
    z=-1

    for j in range(0, 100, 1):
        z=z+1
        for i in range(j*15, (j+1)*15, 1):
            if(i == x):
                tempfarb=farbehum[z]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} mBar'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('Druck', [{'value': x, 'max_value': 1500}])
    gauge.render_to_file('BarHalfGauge.svg')

def drawLux():
    x=1490
    tempfarb='#000000'
    z=-1

    for j in range(0, 100, 1):
        z=z+1
        for i in range(j*20, (j+1)*20, 1):
            if(i == x):
                tempfarb=farbehum[z]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} lux'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('Beleuchtung', [{'value': x, 'max_value': 2000}])
    gauge.render_to_file('LuxHalfGauge.svg')

def drawBat():
    x=90
    wert=100-x
    tempfarb='#000000'


    for j in range(0, 100, 1):
        tempfarb=farbebat[wert]

    dark_lighten_style = LightenStyle(tempfarb)
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=dark_lighten_style)
    percent_formatter = lambda x: '{:.10g} %'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add('Batterie', [{'value': x, 'max_value': 100}])
    gauge.render_to_file('BatHalfGauge.svg')


drawTemp()
drawHumidity()
drawBar()
drawLux()
drawBat()

