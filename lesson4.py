# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, number_of_hours, cost_per_hour, bonus = argv

try:
    salary = float(number_of_hours) * float(cost_per_hour) + float(bonus)
    print(f'Заработная плата сотрудника составила {salary} рублей.')
except ValueError:
    print('Введен неверный формат данных')

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
from random import randint

list_number = [randint(1, 55) for i in range(1, 21)]
new_list_number = [el for el in list_number if list_number[list_number.index(el)] > list_number[list_number.index(el)-1]
                   and list_number.index(el) != 0]
print(list_number)
print(new_list_number)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from random import randint

random_list = [randint(0, 25) for i in range(1, 26)]
new_list_from_random_list = [el for el in random_list if random_list.count(el) == 1]
print(random_list)
print(new_list_from_random_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

even_numbers = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, even_numbers))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

my_list = ['красный', 'желтый', 'зеленый', 'желтый']
i = 0
for el in cycle(my_list):
    if i > 7:
        break
    else:
        print(el)
        i += 1

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from itertools import count
from math import factorial

n = 0
def fact(n):
    for el in count(1):
        yield factorial(el)


for el in fact(n):
    if n < 10:
        print(el)
        n += 1
    else:
        break