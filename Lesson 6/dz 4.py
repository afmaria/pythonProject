"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.
"""
class Car:
    
    def __init__(self,speed, color, name, is_police= False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = speed
        
    def go(self):
        return print(f'{self.name} поехала')
    
    def turn(self, direct):
        return print(f'{self.name} повернула {direct}')
    
    def stop(self):
        return print(f'{self.name} остановилась')
    def on_speed(self):
        return print(f'Скорость {self.name} {self.speed}')
class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

class WorkCar(Car):
    def on_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
            
class TownCar(Car):
    def on_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
            
sport_car = SportCar(80, 'синяя','БМВ', False)
town_car = TownCar(70, 'белая','мазда', False)
work_car = WorkCar(40, 'белая','хендай', False)
police_car = PoliceCar(60,'черная','лада', True)

sport_car.go()
sport_car.on_speed()
town_car.on_speed()
work_car.turn('налево')
town_car.stop()
print(f'Полицейская машина {police_car.color}')
