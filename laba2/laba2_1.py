import numpy as np
from terminaltables import AsciiTable
import matplotlib.pyplot as plt

def func(x):
    # return np.power(x, 3) - 2 * np.power(x, 2) - 4 * x + 5
    # return 2*x-3*((x**2)**(1/3))
    return 24-(2/3)*x+(1/30)*x**2

# a, b, e = -3.0, 0.0, 0.01
# a, b, e = 1.0, 4.0, 0.01
a, b, e = 5.0, 20.0, 1.5
x1, x_data, xi = 0, [], 0
X_cord = np.around(np.arange(start=a, stop=b - 0.001, step=0.1), decimals=5)

if func(a) == 0:
    print(f'Решением уравнения является: {a}\n')
elif func(b) == 0:
    print(f'Решением уравнения является: {b}\n')
else:
    while b - a > e:
        dx = (b - a) / 2
        x1 = a + dx
        if np.sign(func(a)) != np.sign(func(x1)):
            b = x1
        else:
            a = x1
        x_data.append([np.around(x1, decimals=5), np.around(func(x1), decimals=5), np.around(dx, decimals=5)])
    # print(f'Решением уравнения является: {np.around(x1, decimals=5)}\n')
    xi = np.around(x1, decimals=5)

table_data_x = []
for i, item in enumerate(x_data):
    table_data_x.append([f'x{i + 2}', item[0], item[1], item[2]])

table_data_ans = [['x', f'{xi}'], ['F(x)', f'{np.around(func(xi), decimals=5)}']]

gridsize = (7, 21)
fig = plt.figure(figsize=(10, 6), dpi=120, tight_layout=True)
fig.suptitle('720-М2 - Гильфанов Булат Искандерович - Лаб. раб. №2 - 6 вариант', fontsize=16)


ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=13, rowspan=7)
ax1.plot([item for i, item in enumerate(X_cord)], [func(item) for i, item in enumerate(X_cord)], '-.g', label="F(x)")
ax1.legend()
ax1.grid()

ax2 = plt.subplot2grid(gridsize, (0, 14), colspan=7, rowspan=4)
ax2.axis('tight')
ax2.axis('off')
x5_table = ax2.table(cellText=table_data_x, loc="center", cellLoc='left',
                     colLabels=['Шаг', 'x', 'F(x)', '|x(i) - x(i-1)|'])
x5_table.auto_set_font_size(False)
x5_table.auto_set_column_width(col=[0, 1, 2, 3])
x5_table.set_fontsize(9)

ax3 = plt.subplot2grid(gridsize, (4, 14), colspan=7, rowspan=6)
ax3.axis('tight')
ax3.axis('off')
x10_table = ax3.table(cellText=table_data_ans, loc="center", cellLoc='left')
x10_table.auto_set_font_size(False)
x10_table.auto_set_column_width(col=[0, 1, 2, 3])
x10_table.set_fontsize(9)

plt.show()