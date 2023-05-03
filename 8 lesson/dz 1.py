"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

"""
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def number(cls,day_month_year):
        res = day_month_year.split('-')
        print(res)
        day = int(res[0])
        month = int(res[1])
        year = int(res[2])
        print(f'Дата {day} Месяц {month} Год {year}')

    @staticmethod
    def proof_number(day_month_year):
        res = day_month_year.split('-')
        if 0 < int(res[0]) < 32:
            print(f'Дата {int(res[0])}')
        else:
            print("Неверные данные для даты")
        if 0 < int(res[1]) < 13:
            print(f'Месяц {int(res[1])} ')
        else:
            print('Неверные данные для месяца')
        if int(res[2]) > 0:
            print(f'Год {int(res[2])}')
        else:
            print('Неверные данные для года')

Data.number("12-10-1992")
Data.proof_number("25-32-1962")

