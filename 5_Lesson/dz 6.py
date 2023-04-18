"""
Сформировать (не программно) текстовый файл.
В нем каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести на экран.

"""

with open('lesson_2.txt', 'r') as my_file:
    lesson = {}
    for line in my_file:
        my_line = line.replace("(лаб)", "").replace("(л)", "").replace("(пр)", "")
        subject, num_lec, num_pract, num_lab = my_line.split()
        lesson[subject] = int(num_lec) + int(num_lab) + int(num_pract)
        print(f'Количество уроков по предмету {lesson}')





