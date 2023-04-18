"""
Создать текстовый файл. Построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс, вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
"""

my_file = open("workers.txt", "r", encoding='utf-8')
workers = {}
my_line = 0
all_salary = 0
for line in my_file:
    my_line += 1
    last_name, my_salary = line.split()
    salary = int(my_salary)
    all_salary += salary
    if salary < 20000:
        print(last_name)
print(f'Средняя зарплата составляет {all_salary / my_line}')

my_file.close()






