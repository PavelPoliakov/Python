'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат..'''
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'{self.color} {self.name} поехал.')

    def stop(self):
        return print(f'{self.color} {self.name} остановился.')

    def turn_left(self):
        return print(f'{self.color} {self.name} повернул налево.')

    def turn_right(self):
        return print(f'{self.color} {self.name} повернул направо.')

    def turn_around(self):
        return print(f'{self.color} {self.name} развернулся.')

    def show_speed(self, speed):
        return print(f'{self.color} {self.name} движется со скоростью {speed} км/ч')

class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            return print(f'Текущая скорость автомобиля {speed} км/ч. {self.color} {self.name} превысил скорость')
        else:
            return print(f'Текущая скорость автомобиля {speed} км/ч.')

class SportCar(Car):
    def get_away_police(self):
        return print(f'{self.color} {self.name} скрылся от полиции')

class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            return print(f'Текущая скорость автомобиля {speed} км/ч. {self.color} {self.name} превысил скорость')
        else:
            return print(f'Текущая скорость автомобиля {speed} км/ч.')

class PoliceCar(Car):
    def chase(self):
        return print(f'{self.color} {self.name} преследует нарушителя.')

kamaz_car = WorkCar(50, 'Оранжевый', 'КамАЗ')
uaz_car = PoliceCar(90, 'Полицейский', 'Бобик', True)
lamborghini_car = SportCar(360, 'Желтый', 'Lamborghini', False)
hyundai_car = TownCar(140, 'Серый', 'Hyundai', False)
liaz_car = Car(60, 'Синий', 'Бусик', False)
kamaz_car.go()
liaz_car.stop()
lamborghini_car.turn_left()
uaz_car.chase()
lamborghini_car.get_away_police()
hyundai_car.turn_right()
liaz_car.turn_around()
kamaz_car.show_speed(40)
hyundai_car.show_speed(120)
uaz_car.chase()
uaz_car.show_speed(90)
print(uaz_car.is_police)
print(lamborghini_car.is_police)
print(hyundai_car.name)



