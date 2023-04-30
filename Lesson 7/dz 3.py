"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
"""
class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        print(f'Сумма клеток {self.quantity + other.quantity}')

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            print(f'Вычитание клеток {self.quantity - other.quantity}')
        else:
            print(f'Вычитание совершить нельзя')

    def __mul__(self, other):
        print(f'Умножение клеток {self.quantity * other.quantity}')


    def __truediv__(self, other):
        print(f'Деление клеток {self.quantity // other.quantity}')

    def make_order(self, param):
        __str1 = ''
        for i in range(self.quantity // param):
            for t in range(param):
                __str1 += '*'
            __str1 += "\\n"
        for i in range((self.quantity % param)):
            __str1 += '*'
        return __str1

obj_1 = Cell(12)
obj_2 = Cell(15)
obj_3 = Cell(10)

print(obj_1 + obj_2)
print(obj_1 - obj_3)
print(obj_1 * obj_2)
print(obj_1 / obj_2)

print(obj_1.make_order(5))

