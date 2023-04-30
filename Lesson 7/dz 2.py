"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
 одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import abstractmethod, ABC

class MyClass(ABC):
    @abstractmethod
    def coat(self):
        pass
    @abstractmethod
    def suit(self):
        pass

class Clothes(MyClass):
    def __init__(self, el, v, h):
        self.el = el
        self.v = v
        self.h = h
    @property
    def coat(self):
        m_megure = self.v / 6.5 +0.5
        return m_megure

    @property
    def suit(self):
        m_megure = self.h *2 +0.3
        return m_megure

obj = Clothes(2, 3, 5)

print(obj.coat)
print(obj.suit)
print(obj.coat + obj.suit)
