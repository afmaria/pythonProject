"""
Создать текстовый файл. Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские
Новый блок строк должен записываться в новый текстовый файлю
"""
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
result =[]

with open("number.txt", "r", encoding='utf-8') as my_file:
    for i in my_file:
        i= i.split(' ', 1)
        print(i)
        new_file.append(rus[i[0]] + i[1])
print(new_file)
with open('number_rus.txt', 'w') as my_new_file:
    my_new_file.writelines(new_file)

