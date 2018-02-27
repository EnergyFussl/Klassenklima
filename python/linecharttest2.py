import matplotlib.pyplot as plt
import numpy as np

fnx = lambda : np.random.randint(3, 10, 10)
y = np.row_stack((fnx(), fnx(), fnx(), fnx(), fnx())) 

x = np.arange(10) 
y_stack = np.cumsum(y, axis=0)  

fig = plt.figure(figsize=(11,8))
ax1 = fig.add_subplot(111)

ax1.plot(x, y_stack[0,:], label=1)
ax1.plot(x, y_stack[1,:], label=2)
ax1.plot(x, y_stack[2,:], label=3)
ax1.plot(x, y_stack[3,:], label=4)
ax1.plot(x, y_stack[4,:], label=5)
ax1.legend(loc=2)

colormap = plt.cm.gist_ncar 
colors = [colormap(i) for i in np.linspace(0, 1,len(ax1.lines))]
for i,j in enumerate(ax1.lines):
    j.set_color(colors[i])


plt.savefig('smooth_plot.png')
