"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

"""
season = {'Winter': (1, 2, 12), 'Spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}
n_month = int(input("Введите номер месяца в году "))
if n_month in range(1,13):
    for i in season.items():
        if n_month in i[1]:
            print(f'Время года {i[0]}')
            break
else:
    print('Такого месяца нет')

season_list = [['Winter', 1, 2, 12], ['Spring', 3, 4, 5], ['Summer', 6, 7, 8], ['Autumn', 9, 10, 11]]
n_month = int(input("Введите номер месяца в году "))
if n_month in range(1,13):
    for i, el in enumerate(season_list):
        if n_month in el[1:4]:
            print(f'Время года {el[0]}')
            break
else:
    print('Такого месяца нет')

