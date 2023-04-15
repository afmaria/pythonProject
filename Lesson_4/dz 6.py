"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее. 
Подсказка: используйте функцию count() и cycle() 
модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения. 
#### Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
"""
from itertools import count

first_number = int(input('ВВедите начальное число ' ))
last_number = int(input('Введите последнее число '))
def my_count(first_number, last_number):
    return count(first_number)
for el in count(first_number):
    if el > last_number:
        break
    else:
       print(el)

from itertools import cycle
my_list = [1, 2, 3, 5]
my_iter = int(input('Введите количество циклов для повторения '))
n = 0

for i in cycle(my_list):
    if n < my_iter:
        print(my_list)
        n +=1
    else:
        break







