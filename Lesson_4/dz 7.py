"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
"""
from itertools import count

def my_function(n):
    factorial = 1
    for x in count(1):
        if x > n:
            break
        factorial = factorial * x
        yield factorial
n = int(input('введите число для вычисления '))
i = 0
for el in my_function(n):
    i += 1
    print(f"Факториал {i} = {el}")