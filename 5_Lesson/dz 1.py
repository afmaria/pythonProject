"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""
my_file = input('Введите название файла: ')
f = open(my_file, 'w', encoding='utf-8')
while True:
    new_str = input("Введите текст ")
    if new_str == "":
        break
    f.write(f'{new_str}\n')
f.close()


f = open(my_file, 'r')
content = f.read()
print(content)
f.close()





