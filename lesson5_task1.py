# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных будет свидетельствовать пустая строка.
file_obj = open('my_file_task1.txt', 'a')
new_string = input('Введите строку для добавления в файл (чтобы закрыть файл, нажмите Enter):')
while new_string != '':
    file_obj.write(f'{new_string}\n')
    new_string = input('Введите строку для добавления в файл (чтобы закрыть файл, нажмите Enter):')
file_obj.close()
