import numpy as np


def Kramer(matrix_arg, matrix_free_arg, accuracy):
    mas_return = {}
    matrix_ravn = np.array(matrix_free_arg)  # Матрица свободных членов
    matrix = np.array(matrix_arg)
    matrix_T = matrix.T   # Трансонированая матрица коэфицентов
    matrix_copy = matrix_T.copy()
    det_osnov = np.linalg.det(matrix)  # Детерминант основной матрицы
    

    #   Поочередная замена столбцов в основной матрице и расчет корней.
    for i in range(len(matrix)):
        matrix_copy[i] = matrix_ravn
        mas_return.update({(f"x{i+1}"): round(np.linalg.det(matrix_copy) / det_osnov, accuracy)})
        matrix_copy = matrix_T.copy()
    return mas_return

