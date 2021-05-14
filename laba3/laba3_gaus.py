import numpy as np

myA = np.array([[3, 1, -1], [2, 4, 1], [1, -1, 3]])
myB = np.array([6, 9, 4])


# --- вывод системы на экран
def FancyPrint(A, B, selected):
    x_data = []
    for row in range(len(B)):
        x_local_data = []
        for col in range(len(A[row])):
            x_local_data.append("{1:2.1f}{0}".format(" " if (selected is None
                                                             or selected != (row, col)) else "*", A[row][col]))
        x_local_data.append("={1:2.1f}".format(row + 1, B[row]))
        x_data.append(x_local_data)
    print(np.array(x_data))


# --- перемена местами двух строк системы
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


# --- деление строки системы на число
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


# --- сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


# --- решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(A, B):
    column = 0
    while (column < len(B)):
        print("\nИщем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        FancyPrint(A, B, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            SwapRows(A, B, current_row, column)
            FancyPrint(A, B, (column, column))
        print("Нормализуем строку с найденным элементом:")
        DivideRow(A, B, column, A[column][column])
        FancyPrint(A, B, (column, column))
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        FancyPrint(A, B, (column, column))
        column += 1
    print("\nМатрица приведена к треугольному виду, считаем решение")
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print(f"\nПолучили ответ: {X}")
    return X


print(f"""
720-М2 - Гильфанов Б. И.
Лабораторная работа - 5 - Гаусс
Вариант - 6
\nМатрица A = \n{myA}
\nМатрица b = \n{myB}""")
Gauss(myA, myB)