import numpy as np


def Gauss(matrix_table, accuracy):

    mas_return = {}

    #   Расширенная матирица с коэффицентами неизвестных.
    matrix = np.array(matrix_table)

    # Словарь для ответов.
    for i in range(1, len(matrix[0])):
        mas_return.update({(f"x{i}"): None})

    #   Проверка, явлеется ли первый элемент матрицы нулём, если да,
    # то строка заменяется на ту, в которой первый элемен не равен нулю.
    if matrix[0, 0] == 0:
        for i in range(1, len(matrix)):
            print(matrix)
            if matrix[i, 0] != 0:
                matrix[[i, 0]] = matrix[[0, i]]

    #   Перебор матрицы и приведение к треугольному виду.
    for i in range(len(matrix[0])):  # столбцы
        for j in range(1, len(matrix)):  # строки
            if i+j < len(matrix):
                matrix[j+i] = matrix[j+i]*matrix[i, i] + \
                    matrix[i]*matrix[j+i, i]*(-1)

    #   Зануление лишних коэффицентов матрицы.
    for j in range(len(matrix)-1):
        for i in range(j+1, len(matrix[0])-1):
            matrix[j] = matrix[j]*matrix[i, i] + matrix[i]*matrix[j, i]*(-1)

    #   Расчет корня и добавление его в словарь ответов.
    for i in range(1, len(matrix[0])):
        mas_return[(f"x{len(matrix[0])-i}")] = round(matrix[len(matrix)-i,
        len(matrix[0])-1] / matrix[len(matrix)-i, len(matrix[0])-1-i], accuracy)
    return mas_return
