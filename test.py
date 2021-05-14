import numpy as np
import sympy
from pylab import *
from sympy import *
from scipy.optimize import minimize_scalar
from terminaltables import AsciiTable

func = lambda x, y: x ** 2 + y ** 2 + x * y - 3 * x - 6 * y

z_str = 'a[0] ** 2 + a[1] ** 2 + a[0] * a[1] - 3 * a[0] - 6 * a[1]'
exec('z = lambda a: ' + z_str)

z_str = z_str.replace('a[0]', 'x')
z_str = z_str.replace('a[1]', 'y')


def z_grad(a):
    x = Symbol('x')
    y = Symbol('y')

    z_d = eval(z_str)  # exec ('z_d =  ' + z_str)

    yprime = z_d.diff(y)
    dif_y = str(yprime).replace('y', str(a[1]))
    dif_y = dif_y.replace('x', str(a[0]))
    yprime = z_d.diff(x)
    dif_x = str(yprime).replace('y', str(a[1]))
    dif_x = dif_x.replace('x', str(a[0]))

    return np.array([eval(dif_y), eval(dif_x)])


def mininize(a):
    l_min = minimize_scalar(lambda l: z(a - l * z_grad(a))).x
    return a - l_min * z_grad(a)


def norm(a):
    return math.sqrt(a[0] ** 2 + a[1] ** 2)


dot = [np.array([1.0, 4.0])]
dot.append(mininize(dot[0]))

eps = 0.05

while norm(dot[-2] - dot[-1]) > eps: dot.append(mininize(dot[-1]))

data = [['i', 'x1', 'x2', 'f(x1,x2)']]

for i, item in enumerate(dot):
    data.append([i, item[0], item[1], func(item[0], item[1])])

table = AsciiTable(data)
print(table.table)