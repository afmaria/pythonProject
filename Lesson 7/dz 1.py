"""
 Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
 принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_list = ""
        for el in self.matrix:
            my_list += " ".join(map(str,el)) + "\n"
            return my_list

    def __add__(self, other):
        matrix_sum = []
        for el1, el2 in zip(self.matrix, other.matrix):
            ind_sum = []
            for in1, in2 in zip(el1, el2):
                ind_sum.append(int(in1) + int(in2))
                matrix_sum.append(ind_sum)
            return Matrix(matrix_sum)


obj_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(obj_1)
obj_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(obj_2)
print(obj_2 + obj_1)

