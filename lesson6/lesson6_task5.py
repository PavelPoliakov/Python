'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра..'''
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Для создания рисунка используется инструмент {self.title}')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запущена отрисовка жирной линии')

black_pen = Pen('Черная ручка')
my_pencil = Pencil('Мягкий карандаш')
my_handle = Handle('Маркер')
brush = Stationery('Кисточка')
black_pen.draw()
my_pencil.draw()
my_handle.draw()
brush.draw()
