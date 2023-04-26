"""
 Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""
class Workers:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}

class Position(Workers):
    def full_name(self):
        return f'{self.name} {self.surname}'
    def workers_income(self):
        return f'{sum(self.income.values())}'

obj = Position ("Иван","Иванов","Тестировщик",50000, 5000)
print(obj.name)
print(obj.surname)
print(obj.position)
print(obj.full_name())
print(obj.workers_income())