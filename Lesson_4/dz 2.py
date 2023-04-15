"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

from functools import reduce

def generator(my_list):
    new_list = []
    for i in range(0,len(my_list)-1):
        if my_list[i+1] > my_list[i]:
            new_list.append(my_list[i+1])
    return new_list

my_list = [5, 2, 3, 10, 12, 11, 20, 25, 8 ]
print(generator(my_list))


