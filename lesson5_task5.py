# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.
with open('my_file_task5.txt', 'w') as file_obj:
    file_obj.writelines(input('Введите через пробел набор чисел для записи в файл:'))

with open('my_file_task5.txt', 'r') as file_obj_r:
    for line in file_obj_r.readlines():
        sum_of_number = sum(map(int, line.rstrip('/n').split()))
    print(f'Сумма всех чисел в файле составит: {sum_of_number}')
