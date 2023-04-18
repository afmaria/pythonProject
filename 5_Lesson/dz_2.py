"""
Создать текстовый файл, сохранить в нем несколько строк, выполнить подсчет строк и слов в каждой строке
"""
my_file = open("text.txt", "r", encoding='utf-8')

my_line = 0
my_word = 0
for i in my_file:
    my_line += 1
    my_word += len(i.split())
print(f'Количество строк {my_line}')
print(f'Количество слов {my_word}')

my_file.close()
