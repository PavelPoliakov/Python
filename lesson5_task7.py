# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open('my_file_task7.txt', 'r') as file_obj:
    firm_dict = {}
    average_profit_dict = {}
    firm_list = []
    number_of_firm = 0
    sum_profit = 0
    for line in file_obj.readlines():
        firm_name, ownership, revenue, expense = line.rstrip('\n').split()
        profit = int(revenue) - int(expense)
        firm_dict[firm_name] = profit
        if profit > 0:
            number_of_firm += 1
            sum_profit += profit
    try:
        average_profit = sum_profit / number_of_firm
        average_profit_dict['average_profit'] = average_profit
    except ZeroDivisionError:
        print('Все компании работают в убыток')
    firm_list.append(firm_dict)
    firm_list.append(average_profit_dict)
    print(firm_list)
with open('task7.json', 'w') as new_json_file_obj:
    json.dump(firm_list, new_json_file_obj)