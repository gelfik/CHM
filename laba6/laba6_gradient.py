import numpy as np
from terminaltables import AsciiTable


def func(x, y):
    return x ** 2 + y ** 2 + x * y - 3 * x - 6 * y


eps, x0, y0, h = 0.05, 1, 4, 0.2


def find_new_x(x, y):
    return x - h * (2 * x + y - 3)


def find_new_y(y, x):
    return y - h * (2 * y + x - 6)


def gradient(x, y):
    i, local_data = 1, [['i', 'x1', 'x2', 'f(x1,x2)']]
    x_old = x
    x = find_new_x(x, y)
    y = find_new_y(y, x_old)
    local_data.append([i, x, y, func(x, y)])
    while np.abs(2 * x + y - 3) > eps and np.abs(2 * y + x - 6) > eps:
        i += 1
        x_old = x
        x = find_new_x(x, y)
        y = find_new_y(y, x_old)
        local_data.append([i, x, y, func(x, y)])
    return local_data


table = AsciiTable(gradient(x0, y0))

print(f"""
720-М2 - Гильфанов Б. И.
Лабораторная работа - 6 - Градиентный спуск
Вариант - 6

{table.table}""")