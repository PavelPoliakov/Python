# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Делить на 0 нельзя')


print(div(float(input('Введите делимое число:')), float(input('Введите делитель:'))))

# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
def person_information(first_name, last_name, year_of_birth, city, email, phone):
    return f'{first_name} {last_name}, {year_of_birth} года рождения. Проживает в городе {city}. email: {email}, ' \
           f'телефон: {phone}'


print(person_information(first_name='Павел', last_name='Поляков', year_of_birth=1988, city='Щёлково',
                         email='scor3.14on@mail.ru', phone='89778603918'))

# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.
def my_func1(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-1] + my_list[-2]


print(my_func1(8, 6, 5))

# Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x
# в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func_exp_1var(x, y):
    return x ** y


print(my_func_exp_1var(3, -5))
# второй вариант
def my_func_exp_2var(x, y):
    result = 1
    for i in range(1, abs(y) + 1):
        result *= (1 / x)
    return result


print(my_func_exp_2var(3, -5))

# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь
# введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.
def sum_all_numbers():
    list_numbers_from_string_numbers = []
    my_sum = 0
    while '/' not in list_numbers_from_string_numbers:
        string_numbers = input(
            'Введите строку чисел, разделенных пробелом (Для завершения работы программы изпользуйте '
            'специальный символ "/":')
        list_numbers_from_string_numbers = list(string_numbers.split(' '))
        if '/' not in list_numbers_from_string_numbers:
            try:
                list_numbers = [int(i) for i in list_numbers_from_string_numbers]
                my_sum += sum(list_numbers)
            except ValueError:
                print('Вы ввели недопустимый символ')
        else:
            try:
                last_list_numbers = [int(i) for i in
                                     list_numbers_from_string_numbers[:list_numbers_from_string_numbers.index('/')]]
                my_sum += sum(last_list_numbers)
            except ValueError:
                print('Вы ввели недопустимый символ')
        print(my_sum)
    return my_sum


sum_all_numbers()

# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(string):
    return string.title()


print(int_func('text'))
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Используйте написанную ранее функцию int_func().
print(int_func('some text and some l e t t e r s'))
