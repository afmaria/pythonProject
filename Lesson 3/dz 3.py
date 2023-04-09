"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""
arg_1 = int(input("Введите число "))
arg_2 = int(input("Введите число "))
arg_3 = int(input("Введите число "))

def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_2 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_3 and arg_2 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_3 + arg_2

print(my_func(arg_1, arg_2, arg_3))
