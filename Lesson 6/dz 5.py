"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.titel = title

    def draw(self):
        print(f'Запуск отрисовки {self.titel}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.titel} ручка')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.titel} карандаш')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.titel} маркер')

obj = Stationery('Отрисовка')

pen = Pen('шариковая')
pen.draw()
pencil = Pencil('цветной')
pencil.draw()
handle = Handle('черный')
handle.draw()



