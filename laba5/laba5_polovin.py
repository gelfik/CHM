import math
import numpy as np
import matplotlib.pyplot as plt

func =  lambda x: 2*x-3*((x**2)**(1/3))

a, b, e, x_data, i = 1, 5.0, 0.001, [], 0

# def half_divide_method(a, b, f):
#     x = (a + b) / 2
#     while math.fabs(f(x)) >= e:
#         x = (a + b) / 2
#         a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
#     return (a + b) / 2


X_cord = np.around(np.arange(start=a, stop=b - 0.001, step=0.0001), decimals=6)

x = (a + b) / 2
x_data.append([i, x, func(x), a, b, func(a) * func(x), math.fabs(func(x))])
while math.fabs(func(x)) >= e:
    i += 1
    x = (a + b) / 2
    a, b = (a, x) if func(a) * func(x) < 0 else (x, b)
    x_data.append([i, x, func(x), a, b, func(a) * func(x), math.fabs(func(x))])

if math.fabs(func(x)) != 0:
    i += 1
    x = (a + b) / 2
    x_data.append([i, x, func(x), a, b, func(a) * func(x), math.fabs(func(x))])

for i, item in enumerate(x_data):
    print(item)

gridsize = (7, 21)
fig = plt.figure(figsize=(10, 6), dpi=120, tight_layout=True)
fig.suptitle('720-М2 - Гильфанов Булат Искандерович - Лаб. раб. №5 Половин. делен. - 6 вариант', fontsize=16)

ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=21, rowspan=5)
ax1.plot([x for x in X_cord], [func(x) for x in X_cord], '-.g', label="2x-3*(x^2)^(1/3)")
ax1.legend()
ax1.grid()
#
# ax2 = plt.subplot2grid(gridsize, (5, 0), colspan=21, rowspan=3)
# ax2.axis('tight')
# ax2.axis('off')
# x5_table = ax2.table(cellText=x_data, loc="center", cellLoc='left',
#                      colLabels=['n', 'xn', 'F(xn)', "F'(xn)", "F(xn)/F'(xn)"])
# x5_table.auto_set_font_size(False)
# x5_table.set_fontsize(9)
plt.show()