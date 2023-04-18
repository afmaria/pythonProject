"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json
profit = {}
my_profit = {}
f_profit = 0
i = 0
profit_avr = 0
firms_profit = []
with open("firms.txt") as my_file:
    for line in my_file:
        f_name, f_form,f_revenue, f_cost = line.split()
        profit[f_name] = int(f_revenue) - int(f_cost)
        if profit.setdefault(f_name) >= 0:
             f_profit = f_profit + profit.setdefault(f_name)
             i =+ 1
    if i != 0:
        profit_avr = f_profit / i
        print(f'средняя прибыль {profit_avr}')
    my_profit = {f'Средняя прибыль': round(profit_avr)}
    profit.update(my_profit)
    print(f'Прибыль компании {profit}')

with open("firms.json", "w") as write_f:
    json.dump(profit, write_f)
