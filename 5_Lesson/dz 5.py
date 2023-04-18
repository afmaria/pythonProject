"""
Создать текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна посчитать сумму чисел в файле и выводить ее на экран
"""
with open("new_file.txt", "w", encoding='utf-8') as my_file:
    my_str = input('Введите цифры через пробел ')
    my_file.writelines(my_str)
    my_items = my_str.split()
print(f'Сумма чисел {sum(map(int, my_items))}')
