import numpy as np
import math
import matplotlib.pyplot as plt
from terminaltables import AsciiTable

func = lambda x: 2 * x - 3 * ((x ** 2) ** (1 / 3))
gr = (math.sqrt(5) + 1) / 2
a, b, e, x_data, i = -1, 5, 0.01, [['Шаг', 'a', 'x1', 'x2', 'b', 'F(x1)', 'F(x2)', 'b-a']], 0

X_cord = np.around(np.arange(start=a, stop=b - 0.001, step=0.0001), decimals=6)

c = b - (b - a) / gr
d = a + (b - a) / gr
x_data.append(
    [i, np.around(a, decimals=6), np.around(c, decimals=6), np.around(d, decimals=6), np.around(b, decimals=6),
     np.around(func(c), decimals=6), np.around(func(d), decimals=6), np.around(b - a, decimals=6)])
i += 1
while abs(b - a) > e:
    if func(c) < func(d):
        b = d
    else:
        a = c
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    x_data.append(
        [i, np.around(a, decimals=6), np.around(c, decimals=6), np.around(d, decimals=6), np.around(b, decimals=6),
         np.around(func(c), decimals=6), np.around(func(d), decimals=6), np.around(b - a, decimals=6)])
    i += 1

gridsize = (7, 21)
fig = plt.figure(figsize=(10, 6), dpi=120, tight_layout=True)
fig.suptitle('720-М2 - Гильфанов Булат Искандерович - Лаб. раб. №5 Золотое сеч. - 6 вариант', fontsize=16)

ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=21, rowspan=3)
ax1.plot([x for x in X_cord], [func(x) for x in X_cord], '-.g', label="2x-3*(x^2)^(1/3)")
ax1.legend()
ax1.grid()
ax2 = plt.subplot2grid(gridsize, (3, 0), colspan=21, rowspan=3)
ax2.axis('tight')
ax2.axis('off')
x5_table = ax2.table(cellText=x_data, loc="center", cellLoc='left')
x5_table.auto_set_font_size(False)
x5_table.set_fontsize(9)
ax3 = plt.subplot2grid(gridsize, (6, 0), colspan=21, rowspan=1)
ax3.text(0, 0.5,
         f'Решением является: x={np.around((b + a) / 2, decimals=6)}, F(x)={np.around(func((b + a) / 2), decimals=2)}',
         fontsize=14)
# ax3.axis('tight')
ax3.axis('off')
plt.show()
