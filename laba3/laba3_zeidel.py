import numpy as np
from terminaltables import AsciiTable


def zeidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)
    x_data = [['n', 'x1', 'x2', 'x3', 'eps']]
    i_n = 0
    converge = False

    while not converge:

        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        sum_eps = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n)))
        converge = sum_eps <= eps
        if i_n == 0:
            x_data.append([i_n, x[0], x[1], x[2], sum_eps])
            i_n += 1
        x = x_new
        x_data.append([i_n, x[0], x[1], x[2], sum_eps])
        i_n += 1
    return x, x_data


a = np.array([[3, 1, -1], [2, 4, 1], [1, -1, 3]])
b = np.array([[6], [9], [4]])
# a = np.array([[3,0,-1], [2,-5,1], [2,2,5]])
# b = np.array([[7], [-2], [1]])
eps = 0.01

answ, x_data = zeidel(a, b, eps)
table = AsciiTable(x_data)

print(f"""
720-М2 - Гильфанов Б. И.
Лабораторная работа - 3 - Зейдел
Вариант - 6
\nМатрица A = \n{a}
\nМатрица b = \n{b}
\n{table.table}
\nОтветом данного задания является: {answ}, при точности {eps}""")
