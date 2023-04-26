"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
"""
class Road:
    normal_weight = 100
    tickness = 10

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def weight_of_road(self):
        return  self._lenght * self._width * self.normal_weight * self.tickness


obj = Road(2000, 30)
obj.weight_of_road()

print(obj.weight_of_road())
