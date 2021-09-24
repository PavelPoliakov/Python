# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
file_obj = open('my_file_task3.txt', 'r')
employees_dict = {}
number_employees = 0
for line in file_obj.readlines():
    last_name, salary = line.rstrip('\n').split()
    employees_dict[last_name] = float(salary)
    number_employees += 1
print(employees_dict)
print(f'В компании работает {number_employees} сотрудников')
for key, value in employees_dict.items():
    if value < 20000.00:
        print(f'У сотрудника {key} оклад менее 20000 рублей и составляет {value} рублей')
sum = 0
for value in employees_dict.values():
    sum += value
average_salary = sum / number_employees
print(f'Средняя величина дохода сотрудников составляет: {average_salary} рублей')
file_obj.close()