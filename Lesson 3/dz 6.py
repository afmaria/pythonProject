"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

my_str = input("Введите текст ").split()
def int_func(my_str):
    return my_str.title()

for i in range(0, len(my_str)):
    print(int_func(my_str[i]), end=' ')
