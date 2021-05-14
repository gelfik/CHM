import numpy as np
from scipy import misc #Производная
import matplotlib.pyplot as plt


def func(x):
    return 3 * x - 14 + np.exp(x) - np.exp(-1 * x)
    # return 1-x+np.sin(x)-np.log(1+x)

def func_proiz(x):
    return misc.derivative(func, x, dx=1e-8)


a, b, e, x_data, i = 2, 2.3, 0.01, [], 0
# a, b, e, x_data, i = 1, 2, 0.01, [], 0
x = (a + b) / 2
xn = x - (func(x) / func_proiz(x))

X_cord = np.around(np.arange(start=a, stop=b - 0.001, step=0.0001), decimals=6)
while True:
    x_data.append([i, np.around(xn, decimals=6), np.around(func(x), decimals=5), np.around(func_proiz(x), decimals=5),
                   np.around(func(x) / func_proiz(x), decimals=5)])
    if np.abs(func(x) / func_proiz(x)) < e: break
    x = xn
    xn = x - (func(x) / func_proiz(x))
    i += 1

gridsize = (7, 21)
fig = plt.figure(figsize=(10, 6), dpi=120, tight_layout=True)
fig.suptitle('720-М2 - Гильфанов Булат Искандерович - Лаб. раб. №2 Ньютон - 6 вариант', fontsize=16)

ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=21, rowspan=5)
ax1.plot([item for i, item in enumerate(X_cord)], [-np.exp(item)+np.exp(-item) for i, item in enumerate(X_cord)], '-.g', label="(-e^x)+(e^(-x))")
ax1.plot([item for i, item in enumerate(X_cord)], [3*item-14 for i, item in enumerate(X_cord)], '-.r', label="3*x-14")
ax1.legend()
ax1.grid()

ax2 = plt.subplot2grid(gridsize, (5, 0), colspan=21, rowspan=3)
ax2.axis('tight')
ax2.axis('off')
x5_table = ax2.table(cellText=x_data, loc="center", cellLoc='left',
                     colLabels=['n', 'xn', 'F(xn)', "F'(xn)", "F(xn)/F'(xn)"])
x5_table.auto_set_font_size(False)
x5_table.set_fontsize(9)
plt.show()